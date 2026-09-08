#!/usr/bin/env python3
from __future__ import annotations

from urllib.parse import parse_qs, urlparse

SENSITIVE_PATH = ("/unsubscribe", "/退订", "/preferences", "/manage-subscription", "/login", "/signin")
SENSITIVE_QUERY = {"token", "auth", "access_token", "unsubscribe", "email_token"}


def is_sensitive(url: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path.lower()
    if any(marker in path for marker in SENSITIVE_PATH):
        return True
    return bool(SENSITIVE_QUERY.intersection(parse_qs(parsed.query)))
