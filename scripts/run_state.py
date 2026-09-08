#!/usr/bin/env python3
"""Small, atomic state store for one newsletter intake mailbox."""
from __future__ import annotations

import json
import os
import tempfile
import time
import uuid
from contextlib import contextmanager
from pathlib import Path


class StateError(RuntimeError):
    pass


@contextmanager
def _operation_lock(path: str | Path):
    lock = Path(path).with_suffix(Path(path).suffix + ".lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise StateError("state is being updated by another process") from exc
    try:
        os.close(fd)
        yield
    finally:
        try:
            lock.unlink()
        except FileNotFoundError:
            pass


def load(path: str | Path) -> dict:
    p = Path(path)
    if not p.exists():
        return {"processed_message_ids": [], "delivery": "not_sent"}
    value = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise StateError("state must be a JSON object")
    return value


def save(path: str | Path, state: dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{p.name}.", dir=p.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_name, p)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def begin_run(path: str | Path, mode: str) -> str:
    with _operation_lock(path):
        state = load(path)
        active = state.get("active_run")
        if active:
            raise StateError(f"run already active: {active['run_id']}")
        run_id = uuid.uuid4().hex
        state["active_run"] = {"run_id": run_id, "mode": mode, "started_at": int(time.time())}
        state["delivery"] = "not_sent"
        save(path, state)
        return run_id


def finish(path: str | Path, run_id: str, message_ids: list[str], cutoff: str, *, delivery: str) -> None:
    if delivery not in {"sent", "chat_only", "unknown"}:
        raise StateError("delivery must be sent, chat_only, or unknown")
    with _operation_lock(path):
        state = load(path)
        active = state.get("active_run")
        if not active or active.get("run_id") != run_id:
            raise StateError("run is not active")
        state["delivery"] = delivery
        if delivery != "unknown":
            state["last_successful_cutoff"] = cutoff
            old = set(state.get("processed_message_ids", []))
            state["processed_message_ids"] = sorted(old | set(message_ids))
        state.pop("active_run", None)
        save(path, state)
