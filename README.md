# 订阅邮件精选

简体中文 | [English](README.en.md) | [日本語](README.ja.md)

**每日从 Gmail 订阅邮件提炼一份有价值的晨报或晚报。** 不用一封封邮件点开，也不会遗漏重要信息。

适用于 Claude Code、Codex、Cursor、Grok Bot 等 AI Agent。

## 安装

**方式一：发给 Agent（推荐）**

```text
请安装 gmail-newsletter-digest：https://github.com/candybox-ai/gmail-newsletter-digest
```

**方式二：命令行**（需 Node.js）

```bash
npx skills add candybox-ai/gmail-newsletter-digest
```

也可克隆到当前工具的 skills 目录：

```bash
git clone https://github.com/candybox-ai/gmail-newsletter-digest.git ~/.claude/skills/gmail-newsletter-digest
```

## 触发方式

- 帮我从邮件订阅做一份今天的晨报
- 做一份晚报，用中文，发到我平时收简报的邮箱
- 先帮我连好 Gmail，再一起确认要跟踪哪些订阅
- 将晨报发送时间调整为早上 9:30

## 设置

安装成功后，按下面步骤完成设置（每步由你确认）：

1. **连接 Gmail** — 连接你的 Gmail 账户
2. **确认订阅范围** — 选出要跟踪的 newsletter
3. **设定时间与语言** — 晨报 / 晚报几点出，正文用中文还是英文
4. **设定投递方式** — 直接显示在对话中，或发送到指定邮箱

## 依赖

- **Gmail**：读取订阅邮件；若要把简报发到邮箱，再开启发送权限
- **Python 3**：由 Agent 完成，无需手动操作

## 隐私

- 订阅范围、可选阅读偏好、语言和收件地址，只保存在运行该 Agent 的环境中，本仓库不收集这些数据。
- 本 skill 只读取你的订阅邮件，并在你启用邮件投递后发送成品简报；不会转发、删除或改动邮箱里的已有邮件。

## 许可证

MIT — 见 [LICENSE](LICENSE)。

## 反馈

https://github.com/candybox-ai/gmail-newsletter-digest/issues

## 致谢

本仓库由 Grok Bot 协助发布与整理。
