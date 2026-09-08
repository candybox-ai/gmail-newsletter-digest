# 订阅邮件精选

简体中文 | [English](README.en.md) | [日本語](README.ja.md)

从 Gmail 订阅邮件整理晨报和晚报，在确认的订阅与时间范围内保留重要信息，按需展开。

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
- 多展开技术细节，重要信息仍全部保留（可选呈现偏好）

## 快速开始

首次使用请按顺序完成设置（Setup），每步确认后再进入下一步：

1. **连接 Gmail** — 授权从指定 Gmail 账户读取订阅邮件
2. **确认订阅范围** — 从近期邮件中选择要跟踪的 newsletter，也可补充低频订阅，最终由你确认
3. **设定生成时间与正文语言** — 同一步确认时间、时区和语言；正文支持中文、英文
4. **设定投递方式** — 默认在对话中交付，可指定简报收件邮箱

仅在对话中一次性生成时：完成步骤 1–2，并确定正文语言即可；定时生成与邮件投递可之后再设。

无需填写用户画像。可选偏好只影响排序和展开，不影响重要信息收录。先逐封登记信息点，再合并和核对；重点解读最多 3 条，其余重要信息进入不限条数的「重要简讯」。没有公开链接但有邮件原文依据时，保留摘要并注明受限来源。覆盖限于确认的订阅与时间窗口，格式校验不能保证语义上绝对无遗漏。

## 依赖

- **Gmail 权限（读取必需，发送可选）**：读取指定 Gmail 账户的订阅邮件；只有启用邮件投递时才需要发送权限
- 生成时间按你在设置中设定的时区执行
- **Python 3** 标准库

## 隐私

订阅范围、可选呈现偏好、语言、收件地址等配置，保存在**运行该助手的环境**中（本机或云端工作区）。本 skill 仓库本身不收集这些数据。

本 skill 只读取订阅邮件，并在你启用邮件投递后发送生成好的简报；不转发、不删除、不修改邮箱里的任何邮件。

## License

MIT — 见 [LICENSE](LICENSE)。

## 致谢

本仓库由 Grok Bot 协助发布与整理。
