# 订阅邮件精选

简体中文 | [English](README.en.md) | [日本語](README.ja.md)

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

需要 Node.js：

```bash
npx skills add candybox-ai/gmail-newsletter-digest
```

或直接克隆到**当前工具实际使用的 skills 目录**。例如 Claude Code 常见路径为：

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
- 我是 AI 产品经理，焦点是 Agent；产业并购默认只放速览（读者画像示例）

## 快速开始

首次使用请按顺序完成设置（Setup），每步确认后再进入下一步：

1. **连接 Gmail** — 授权从指定 Gmail 账户读取订阅邮件
2. **设定读者画像（Reader）** — 职业/角色、当前重点关注、默认降级或不关注的类型（提问时会给 2–3 个示例答案；会影响后续必读推荐）
3. **选择必读列表** — 从近期邮件中选出要跟踪的 newsletter；Suggested 会参考 Reader，最终由你确认
4. **设定生成时间与正文语言** — 同一步确认晨报 / 晚报的时间与时区，以及简报正文语言
5. **设定投递方式** — 默认在对话中交付，可指定简报收件邮箱

仅在对话中一次性生成时：完成步骤 1–3，并确定正文语言即可（可用已锁定的语言，或按订阅内容临时估计）；定时生成与邮件投递可之后再设。

## 依赖

- **Gmail 权限（读取必需，发送可选）**：读取指定 Gmail 账户的订阅邮件；只有启用邮件投递时才需要发送权限
- 生成时间按你在设置中设定的时区执行
- **Python 3** 标准库

## 隐私

必读列表、读者画像（角色/焦点/降级偏好）、语言、收件地址等配置与偏好，保存在**运行该助手的环境**中（本机或你使用的云端工作区）。本 skill 仓库本身不收集这些数据。

本 skill 只读取订阅邮件，并在你启用邮件投递后发送生成好的简报；不转发、不删除、不修改邮箱里的任何邮件。

## License

MIT — 见 [LICENSE](LICENSE)。

## 致谢

本仓库由 Grok Bot 协助发布与整理。
