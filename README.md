# 订阅邮件精选（gmail-newsletter-digest）

简体中文 | [English](README.en.md)

从 Gmail 订阅邮件整理出一份值得读的晨报和晚报，不必一封封点开阅读，也不会错过重要信息。

适用于能读写本地文件并执行命令的 AI Agent，如 Claude Code、Codex、Cursor、Grok Bot 等。

## 适合谁

适合邮箱里订阅了大量 newsletter、又没时间逐封读完的人。

## 安装

### 方式一：发给 Agent（需支持从 GitHub 安装 skill）

```text
请安装 gmail-newsletter-digest：https://github.com/candybox-ai/gmail-newsletter-digest
```

若不支持该安装方式，请使用方式二。

### 方式二：命令行

将仓库克隆到**当前工具实际使用的 skills 目录**。例如 Claude Code 常见路径为：

```bash
git clone https://github.com/candybox-ai/gmail-newsletter-digest.git ~/.claude/skills/gmail-newsletter-digest
```

Cursor、Codex、Grok Bot 等请查阅各自文档中的 skill / workflow 路径后克隆到对应目录。

安装后请确认该目录下存在 `SKILL.md`，并在助手的 skill 列表中可见（或按该工具的方式重新加载 skill）。

## 触发方式

安装完成后，可直接对助手说，例如：

- 帮我从邮件订阅做一份今天的晨报
- 做一份晚报，用中文，发到我平时收简报的邮箱
- 先帮我连好 Gmail，再一起选出必读订阅

## 快速开始

首次使用请按顺序完成设置（Setup），每步确认后再进入下一步：

1. **连接 Gmail** — 授权从指定 Gmail 账户读取订阅邮件
2. **选择必读列表** — 从近期邮件中选出要跟踪的 newsletter 并保存
3. **设定生成时间** — 确认晨报 / 晚报的时间与时区
4. **选择正文语言** — 确定简报正文使用的语言
5. **设定投递方式** — 默认在对话中交付，可指定简报收件邮箱

## 依赖

- **Gmail 权限（读取必需，发送可选）**：读取指定 Gmail 账户的订阅邮件；只有启用邮件投递时才需要发送权限
- 生成时间按你在设置中设定的时区执行
- **Python 3** 标准库

## 隐私

必读列表、语言、收件地址等配置与偏好，保存在**运行该助手的环境**中（本机或你使用的云端工作区）。本 skill 仓库本身不收集这些数据。

本 skill 只读取订阅邮件，并在你启用邮件投递后发送生成好的简报；不转发、不删除、不修改邮箱里的任何邮件。

## License

MIT — 见 [LICENSE](LICENSE)。

## 致谢

本仓库由 Grok Bot 协助发布与整理。
