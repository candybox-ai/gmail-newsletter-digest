# 購読メール精選

[简体中文](README.md) | [English](README.en.md) | 日本語

**毎日、Gmail の購読メールから価値のある朝刊または夕刊ダイジェストを抽出します。** 一件ずつ開く必要はなく、重要な情報も逃しません。

Claude Code、Codex、Cursor、Grok Bot などの AI Agent 向けです。

## インストール

**方法 1：Agent に依頼（推奨）**

```text
gmail-newsletter-digest をインストールしてください：https://github.com/candybox-ai/gmail-newsletter-digest
```

**方法 2：コマンドライン**（Node.js が必要）

```bash
npx skills add candybox-ai/gmail-newsletter-digest
```

お使いのツールの skills ディレクトリへクローンすることもできます：

```bash
git clone https://github.com/candybox-ai/gmail-newsletter-digest.git ~/.claude/skills/gmail-newsletter-digest
```

## 起動例

- メール購読から今日の朝刊ダイジェストを作って
- 夕刊を日本語で作り、普段受け取るメールアドレスに送って
- まず Gmail を接続して、追跡する購読を一緒に確定して
- 朝刊の送信時刻を朝 9:30 に変更して

## 設定

インストール後、次の順で設定してください（各ステップはあなたが確認します）：

1. **Gmail を接続** — あなたの Gmail アカウントを接続
2. **購読範囲を確定** — 追跡する newsletter を選ぶ
3. **時刻と言語を設定** — 朝刊 / 夕刊の時刻と、本文を中国語か英語か
4. **配信方法を設定** — 会話内に直接表示する、または指定のメールアドレスへ送信

## 依存関係

- **Gmail**：購読メールを読む。ダイジェストをメールで送る場合のみ送信権限も必要
- **Python 3**：Agent が処理します。手動操作は不要

## プライバシー

- 購読範囲、任意の読書設定、言語、送信先は、Agent が動作する環境にのみ保存されます。このリポジトリはそれらのデータを収集しません。
- この skill は購読メールを読み取り、メール配信を有効にした場合にのみ完成したダイジェストを送信します。転送・削除・受信トレイ内の既存メールの変更は行いません。

## ライセンス

MIT — [LICENSE](LICENSE) を参照。

## フィードバック

https://github.com/candybox-ai/gmail-newsletter-digest/issues

## クレジット

本リポジトリは Grok Bot の支援により公開・整理されました。
