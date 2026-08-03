<div align="center">

# Awesome AI Reverse Engineering

AI 辅助逆向工程工具、MCP、Skill 与 Agent 清单

简体中文 | [English](README_EN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

</div>

## 项目简介

Awesome AI Reverse Engineering 收集 AI 辅助逆向工具，覆盖 JavaScript 与 Web、二进制与原生程序、Android/iOS、浏览器自动化和流量分析。

收录内容包括 MCP 服务器、Skill、IDA Pro/Ghidra/Binary Ninja/JADX 插件、Agent 和桌面工作站。

> **使用范围：** 仅用于自有系统、明确授权的安全测试、数字取证、教育培训和防御性安全研究。

## 工具形态说明

| 形态              | 作用                                          |
| --------------- | ------------------------------------------- |
| MCP Server     | 把浏览器、反编译器、调试器或设备能力提供给 AI 调用                 |
| Skill          | 为 AI 提供分析方法、任务步骤、判断标准和输出规范                  |
| IDE / RE 插件    | 把 AI 能力集成到 IDA、Ghidra、JADX、Binary Ninja 等工具 |
| Agent          | 根据目标规划任务、调用工具、验证结果并生成报告                     |
| 桌面工作站          | 将抓包、浏览器、Hook、AI 分析和结果管理集成在一个应用中             |
| 知识库            | 为 AI 提供漏洞模式、案例和测试思路，但不直接执行分析操作              |

> MCP 连接 AI 与分析工具，Skill 定义分析方法，Agent 负责规划、执行和验证。

## 目录

- [快速选型](#快速选型)
- [JavaScript 与 Web 逆向](#javascript-与-web-逆向)
- [IDA Pro 生态](#ida-pro-生态)
- [二进制与原生程序逆向](#二进制与原生程序逆向)
- [Ghidra 生态](#ghidra-生态)
- [Android 与 iOS 安全分析](#android-与-ios-安全分析)
- [浏览器自动化与流量分析](#浏览器自动化与流量分析)
- [工具评估维度](#工具评估维度)
- [使用规范](#使用规范)
- [贡献指南](#贡献指南)

## 快速选型

| 需求                              | 推荐项目                              |
| ------------------------------- | --------------------------------- |
| 普通网页签名、参数和 Cookie 定位            | [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp)                    |
| 综合型 JS、WASM、AST 和网络分析           | [jshookmcp](https://github.com/vmoranv/jshookmcp)                         |
| Worker、Webpack、JSVMP 等高级 Web 逆向 | [reverse-skill](https://github.com/715494637/reverse-skill/)                     |
| 将浏览器加密函数封装成接口                   | [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill)      |
| 将网站流量转换为可复用 API 客户端              | [reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer)              |
| 强调证据沉淀和本地复现                     | [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP)                    |
| 反检测浏览器环境                        | [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp)               |
| 微信小程序包解密与源码还原                | [wxapkg](https://github.com/wux1an/wxapkg)                                      |
| Windows 微信小程序 F12 调试             | [zhong-wechat-wmpf-debugger](https://github.com/netz888/zhong-wechat-wmpf-debugger) |
| 微信小程序运行时分析                      | [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp)                   |
| IDA Pro 实时 AI 分析                | [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp)                       |
| IDA 文件导出后交给 AI 分析               | [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)                        |
| 无头 IDA 服务                       | [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)                        |
| 多个 IDA 实例并行分析                  | [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp)                 |
| IDA 内直接使用多种 AI 模型              | [WPeGPT](https://github.com/WPeace-HcH/WPeGPT)                               |
| Ghidra GUI 与无头 AI 分析          | [Ghidra MCP Server](https://github.com/bethington/ghidra-mcp)                 |
| radare2 接入 AI Agent              | [Radare2 MCP Server](https://github.com/radareorg/radare2-mcp)                |
| Binary Ninja AI 集成              | [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp)                  |
| x64dbg / x32dbg 动态调试           | [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp)                  |
| Cheat Engine 内存分析              | [Cheat Engine MCP Bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge) |
| 多工具二进制自动化平台                     | [revula](https://github.com/president-xd/revula)                            |
| Android API 提取和调用链分析            | [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) |
| JADX 内交互式 AI 分析                 | [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp)                       |
| Apktool 解包、Smali 分析与重建          | [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)         |
| Android Frida 动态插桩               | [frida-analykit](https://github.com/ZSA233/frida-analykit)                      |
| Charles 流量接入 AI                 | [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp)                |
| 一体化协议分析工作站                      | [Anything Analyzer](https://github.com/Mouseww/anything-analyzer)                 |
| 引擎级 JS、JSVMP、WASM 追踪            | [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse)                   |

## JavaScript 与 Web 逆向

> JavaScript 运行时调试、请求链定位、Hook、混淆还原、WASM、协议分析和本地算法复现。

### 综合型 MCP

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [jshookmcp](https://github.com/vmoranv/jshookmcp) | MCP | 综合型 AI JS 安全分析平台 | 浏览器自动化、CDP、网络监控、JS Hook、WASM、Source Map、AST 变换 | js hook toolkit that all you need | 是 · 2026-07-30 | 暂无 | 1869 |
| [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp) | MCP | 面向真实浏览器运行时的 JS 调试工具 | 请求参数、动态 Cookie、WebSocket、调用链和关键函数定位 | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可选 CloakBrowser。 | 是 · 2026-07-16 | [v4.0.1](https://github.com/zhizhuodemao/js-reverse-mcp/releases/tag/v4.0.1) · 2026-07-10 | 2378 |
| [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP) | MCP / 工作流 | 标准化 Web 逆向流程 | 页面观察、运行时采样、本地复现、补环境和证据沉淀 | JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它 将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、 Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、 加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等 场景 | 是 · 2026-05-31 | [v2.0.4](https://github.com/NoOne-hub/JSReverser-MCP/releases/tag/v2.0.4) · 2026-05-31 | 958 |

### 微信小程序逆向

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [wxapkg](https://github.com/wux1an/wxapkg) | 桌面工具 | 微信小程序包解密与解包 | `.wxapkg` 扫描、解密、解包和源码结构还原 | 跨平台微信小程序反编译 GUI 工具，.wxapkg 文件扫描 + 解密 + 解包工具 | 否 · 2026-04-28 | [v2.0.0](https://github.com/wux1an/wxapkg/releases/tag/v2.0.0) · 2026-04-16 | 3923 |
| [zhong-wechat-wmpf-debugger](https://github.com/netz888/zhong-wechat-wmpf-debugger) | 调试工具 | Windows 微信小程序 F12 调试入口 | WMPF 版本检测、CDP/DevTools 桥接和新旧运行时调试 | WeChatOpenDevTool 微信小程序强制开启开发者工具 | 是 · 2026-07-18 | [v1.3.0](https://github.com/netz888/zhong-wechat-wmpf-debugger/releases/tag/v1.3.0) · 2026-07-18 | 69 |
| [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) | MCP | 微信小程序 CDP 调试工具 | 微信开发者工具、PC 微信小程序、运行时代码和请求分析 | 微信小程序逆向工程 MCP 服务器，让你的 AI 编码助手（如 Claude、Cursor、Antigravity）能够直接通过 Chrome DevTools Protocol (CDP) 调试和分析微信小程序（包括微信开发者工具或 PC 端微信小程序）中的 JavaScript 代码。 | 否 · 2026-04-22 | 暂无 | 129 |

### JS 逆向 Skill

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) | Skill | 基于反检测浏览器的完整 JS 逆向流程 | 网络捕获、源码定位、Hook、算法还原和本地复现 | 🔧 AI-powered JS逆向工程 Skill —— 覆盖加密还原、混淆分析、动态Cookie、WASM逆向、协议对抗等全链路场景，通过 Node.js 实现算法还原与模拟请求。适配 Claude Code / Claude.ai / 其他AI编码工具 | 是 · 2026-07-29 | [v3.4.1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/releases/tag/v3.4.1) · 2026-07-29 | 963 |
| [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) | Skill | JS 逆向成果服务化 | JSRPC、Flask、autoDecoder、请求加密和响应解密 | 结合chrome-devtools-mcp的能力并加上Skill的规范，实现JSRPC+Flask+autoDecoder方案的前端JS逆向自动化分析，提升JS逆向的效率 | 是 · 2026-07-30 | [v2.1](https://github.com/Fausto-404/js-reverse-automation--skill/releases/tag/v2.1) · 2026-07-28 | 542 |
| [reverse-skill](https://github.com/715494637/reverse-skill/) | Skill | 高级 Web 逆向方法库 | JSVMP、Worker、WASM、Webpack、AST 和协议分析 | 面向 Web JS 逆向分析的技能仓库，覆盖请求链定位、运行时诊断、AST 混淆恢复、JSVMP、worker、WASM、webpack/runtime 与协议语义分析。 | 否 · 2026-05-02 | [jsr-skills-15-a3e116e](https://github.com/715494637/reverse-skill/releases/tag/jsr-skills-15-a3e116e) · 2026-05-02 | 323 |
| [xbsReverseSkill](https://github.com/lwjjike/xbsReverseSkill) | Skill 套件 | 模块化 Web 逆向能力 | AST、纯算法、协议分析、浏览器补环境 | Ai逆向的skill目录 | 是 · 2026-07-21 | [v1.0.0](https://github.com/lwjjike/xbsReverseSkill/releases/tag/v1.0.0) · 2026-03-28 | 340 |

### 专用 Web 安全分析工具

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ruishu-mcp](https://github.com/xuange520/ruishu-mcp) | MCP | 动态 WAF 流量研究工具 | 授权环境中的瑞数类动态防护、请求参数和流量分析 | 🚀 专为 AI Agent 打造的瑞数防爬流量净化 MCP 工具 / An MCP Tool for AI Agents to Stealthily Bypass and Purify Ruishu WAF Traffic | 是 · 2026-07-13 | [v1.1.0](https://github.com/xuange520/ruishu-mcp/releases/tag/v1.1.0) · 2026-04-13 | 85 |

## IDA Pro 生态

> IDA Pro 的 MCP 服务、数据导出工具、内置 AI 插件以及多实例分析接口。

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) | IDA 插件 / MCP | AI 直接读取和操作 IDA Pro | 反编译、交叉引用、重命名、注释和类型恢复 | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. | 是 · 2026-07-30 | [1.4.0](https://github.com/mrexodia/ida-pro-mcp/releases/tag/1.4.0) · 2025-10-06 | 11040 |
| [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | IDA 插件 / 导出工具 | 将 IDA 数据导出后交给 AI IDE 分析 | 大规模代码索引、低交互成本分析 | Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP | 是 · 2026-07-26 | 暂无 | 1860 |
| [WPeGPT](https://github.com/WPeace-HcH/WPeGPT) | IDA AI 插件 | 将多种 AI 模型直接嵌入 IDA | 使用 OpenAI、DeepSeek 等模型进行交互式二进制分析 | An IDA plugin for binary file analysis, powered by AI models such as OpenAI and DeepSeek. | 是 · 2026-05-27 | [v3.0](https://github.com/WPeace-HcH/WPeGPT/releases/tag/v3.0) · 2026-05-27 | 1395 |
| [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) | MCP | Rust 实现的无头 IDA 服务 | 服务端部署、自动化流水线 | Headless IDA Pro MCP Server | 是 · 2026-07-27 | [v9.4.1](https://github.com/blacktop/ida-mcp-rs/releases/tag/v9.4.1) · 2026-07-15 | 693 |
| [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) | IDA 插件 / MCP | 通过单个端点管理多个 IDA 实例 | 多二进制并行分析、跨样本函数相似性搜索和恶意软件组件关联 | Multi-instance IDA Pro MCP server — analyze multiple binaries simultaneously through a single MCP endpoint. | 是 · 2026-07-30 | 暂无 | 369 |

## 二进制与原生程序逆向

> radare2、Binary Ninja、动态调试器、内存分析工具以及跨工具逆向 Agent 和自动化平台。

### radare2 生态

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Radare2 MCP Server](https://github.com/radareorg/radare2-mcp) | radare2 插件 / MCP | radare2 官方 Agent 接口 | CLI 与远程会话、无头分析、只读模式、沙箱和自动化流水线 | MCP stdio server for radare2 | 是 · 2026-07-17 | [1.8.4](https://github.com/radareorg/radare2-mcp/releases/tag/1.8.4) · 2026-06-03 | 275 |
| [r2ai](https://github.com/radareorg/r2ai) | radare2 AI 插件 | 在 radare2 内使用本地或远程 LLM | 函数解释、自动命名、漏洞分析、反编译辅助和 ReAct 工作流 | LLM-based reversing for radare2 | 是 · 2026-07-22 | [1.4.0](https://github.com/radareorg/r2ai/releases/tag/1.4.0) · 2026-06-03 | 462 |

### 动态调试与内存分析

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cheat Engine MCP Bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge) | Cheat Engine 桥接 / MCP | AI 驱动的进程内存分析 | 内存扫描、指针链、结构恢复、反汇编和特征码生成 | Connect Cursor, Copilot & Claude AI directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language. | 是 · 2026-08-03 | 暂无 | 1145 |
| [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) | x64dbg 插件 / MCP | 通过 MCP 远程控制 x64dbg 与 x32dbg | 执行控制、断点、内存、寄存器、反汇编和动态调试自动化 | MCP server plugin for x64dbg debugger - enables AI agents and external tools to control debugging via JSON-RPC 2.0 over HTTP/SSE | 是 · 2026-07-18 | [v1.0.10](https://github.com/SetsunaYukiOvO/x64dbg-mcp/releases/tag/v1.0.10) · 2026-07-18 | 341 |

### 其他逆向软件集成

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Rikugan](https://github.com/buzzer-re/Rikugan) | Agent / 插件 | 嵌入 IDA 和 Binary Ninja 的 AI Agent | 在逆向界面中进行连续对话式分析 | A reverse-engineering agent for IDA Pro and Binary Ninja | 是 · 2026-06-15 | [v1.3.2](https://github.com/buzzer-re/Rikugan/releases/tag/v1.3.2) · 2026-06-15 | 665 |
| [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) | Binary Ninja 插件 / MCP | Binary Ninja AI 桥接 | 多目标二进制实时分析 | A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client. | 否 · 2026-04-05 | [v1.2.1](https://github.com/fosdickio/binary_ninja_mcp/releases/tag/v1.2.1) · 2026-03-22 | 412 |

### 通用 Agent、平台与知识库

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | Skill / Router | 安全任务和工具链路由 | 多工具编排、CTF、安全研究和报告生成 | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 &#124; 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 | 是 · 2026-08-03 | [v1.0.0](https://github.com/zhaoxuya520/reverse-skill/releases/tag/v1.0.0) · 2026-07-17 | 14997 |
| [Open ReverseLab](https://github.com/LING71671/open-reverselab) | 实验环境 / 知识库 / MCP | 面向 Agent 的综合逆向实验室 | 授权环境中的 CTF、APK、PE、密码与协议分析工作流 | Agent-native reverse-engineering lab with a 197-article knowledge base, MCP tools, and CTF/APK/PE automation workflows. | 是 · 2026-08-01 | [v1.1.0-windows](https://github.com/LING71671/open-reverselab/releases/tag/v1.1.0-windows) · 2026-07-08 | 967 |
| [revula](https://github.com/president-xd/revula) | MCP 平台 | 通用逆向工程自动化后端 | 静态分析、动态调试、恶意软件和批量处理 | A fully functional and production-grade reverse engineering MCP Server | 是 · 2026-07-10 | 暂无 | 70 |

## Ghidra 生态

> Ghidra 的 MCP 服务、原生扩展、内置 AI 插件、无头自动化接口以及以 Ghidra 为分析后端的 Agent。

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Ghidra MCP Server](https://github.com/bethington/ghidra-mcp) | Ghidra 插件 / MCP | 综合型 Ghidra MCP 服务 | GUI 与无头分析、批量操作、P-code、调试器和团队协作 | Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. GUI plugin + headless server, lazy tool loading, convention enforcement, batch operations, Ghidra Server integration, and Docker deployment. | 是 · 2026-08-03 | [v6.0.0](https://github.com/bethington/ghidra-mcp/releases/tag/v6.0.0) · 2026-07-25 | 3121 |
| [auto-re-agent](https://github.com/Dryxio/auto-re-agent) | Agent / Ghidra 后端 | 自动重建并验证二进制中的 C/C++ 函数 | 反编译证据收集、候选源码生成、构建测试和一致性检查 | Open-source AI reverse-engineering agent using Ghidra and LLMs to reconstruct and validate C/C++ functions from binaries. | 是 · 2026-07-23 | [v0.2.1](https://github.com/Dryxio/auto-re-agent/releases/tag/v0.2.1) · 2026-07-23 | 1271 |
| [reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | Ghidra 插件 / MCP | Ghidra 逆向任务接口 | 反编译、函数与数据类型分析、重命名和注释 | MCP server for reverse engineering tasks in Ghidra 👩‍💻 | 是 · 2026-08-03 | [v7.3.0](https://github.com/cyberkaida/reverse-engineering-assistant/releases/tag/v7.3.0) · 2026-06-13 | 795 |
| [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) | Ghidra 原生扩展 / MCP | Ghidra 内置 MCP 服务 | 原生界面中的实时二进制分析和 Agent 工具调用 | An native MCP server extension for Ghidra | 是 · 2026-08-03 | [2.11.0](https://github.com/symgraph/GhidrAssistMCP/releases/tag/2.11.0) · 2026-08-03 | 687 |
| [GhidraGPT](https://github.com/weirdmachine64/GhidraGPT) | Ghidra AI 插件 | 将多种 LLM 直接集成到 Ghidra | 对话式函数解释、符号命名和 AI 辅助分析 | Integrate LLM models directly into Ghidra for AI-enhanced reverse engineering. | 是 · 2026-07-22 | [v1.4.0](https://github.com/weirdmachine64/GhidraGPT/releases/tag/v1.4.0) · 2026-07-22 | 612 |
| [PyGhidra-MCP](https://github.com/clearbluejar/pyghidra-mcp) | CLI / MCP | 基于 PyGhidra 的命令行 MCP | 无头分析、GUI 共享状态、脚本化任务和自动化流水线 | Python Command-Line Ghidra MCP | 是 · 2026-08-02 | [v0.2.3](https://github.com/clearbluejar/pyghidra-mcp/releases/tag/v0.2.3) · 2026-07-07 | 394 |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Ghidra 插件 / MCP | Ghidra 与 AI 客户端连接 | 反编译、函数分析和符号整理 | MCP Server for Ghidra | 否 · 2025-06-23 | [1.4](https://github.com/LaurieWired/GhidraMCP/releases/tag/1.4) · 2025-06-23 | 9687 |

## Android 与 iOS 安全分析

> APK 反编译、API 提取、动态插桩、设备管理、流量分析和移动安全知识库。

### Android 静态分析与反编译

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Skill | Android 静态分析与 API 提取 | APK、XAPK、JAR、AAR、Retrofit、OkHttp 和调用链分析 | Claude Code skill to support Android app's reverse engineering | 是 · 2026-06-10 | [v1.1.0](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/releases/tag/v1.1.0) · 2026-04-27 | 6647 |
| [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) | JADX 插件 / MCP | JADX 内实时 AI 分析 | APK 代码阅读、漏洞分析和上下文审查 | Plugin for JADX to integrate MCP server | 是 · 2026-05-28 | [v6.4.0](https://github.com/zinja-coder/jadx-ai-mcp/releases/tag/v6.4.0) · 2026-05-28 | 2591 |
| [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) | Apktool / MCP | 通过 AI 操作 Apktool 的解包与重建能力 | Manifest、资源和 Smali 分析，APK 解包、修改与重新构建 | A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites) | 是 · 2026-07-02 | [V3.0.2](https://github.com/zinja-coder/apktool-mcp-server/releases/tag/V3.0.2) · 2026-07-02 | 615 |

### 动态插桩与设备控制

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [frida-analykit](https://github.com/ZSA233/frida-analykit) | Frida 工具包 / MCP | 面向 Android Agent 的动态插桩接口 | Frida 版本管理、底层工具封装、Hook 和运行时分析 | Frida 工具包 - 主要面向安卓端逆向，解决frida环境版本管理和对Agent端常用底层工具方法封装，支持MCP。（目前主要由AI开发维护代码） | 是 · 2026-05-16 | [v2.1.4](https://github.com/ZSA233/frida-analykit/releases/tag/v2.1.4) · 2026-05-14 | 150 |
| [iOS MCP](https://github.com/witchan/ios-mcp) | MCP | 越狱 iOS 设备控制 | 应用、文件、日志、HID 和辅助功能操作 | iOS MCP: MCP management tool for jailbroken iPhones, enabling developers and AI agents to inspect and control devices. | 是 · 2026-07-30 | [v1.2.3](https://github.com/witchan/ios-mcp/releases/tag/v1.2.3) · 2026-07-30 | 588 |

## 浏览器自动化与流量分析

> 浏览器控制、反检测环境、代理抓包、协议分析和一体化逆向工作站。

| 项目 | 形态 | 核心定位 | 适用场景 | GitHub 简介 | 最近更新 | 最新 Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer) | Agent / CLI | 将网站实际调用的端点生成类型化 API 客户端 | 浏览器流量捕获、接口发现、HAR 分析和 Python/JS/TS 客户端生成 | The agent that turns websites into APIs! | 是 · 2026-07-31 | [v0.13.0](https://github.com/kalil0321/reverse-api-engineer/releases/tag/v0.13.0) · 2026-07-27 | 911 |
| [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp) | MCP | 反检测和隐私浏览器自动化 | 指纹控制、代理、多会话隔离和真实浏览器环境 | 暂无简介 | 是 · 2026-07-25 | [v2.3.0](https://github.com/whit3rabbit/camoufox-mcp/releases/tag/v2.3.0) · 2026-07-06 | 39 |
| [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) | MCP | Charles Proxy AI 接入 | 实时流量、历史 Session 和请求分析 | Charles Proxy MCP server for AI agents with live capture, structured traffic analysis, and agent-friendly tool contracts | 是 · 2026-06-23 | [v3.0.3](https://github.com/heizaheiza/Charles-mcp/releases/tag/v3.0.3) · 2026-04-21 | 289 |
| [CipherBridge](https://github.com/CuriousLearnerDev/CipherBridge) | 桌面工作站 / AI Agent | AI 辅助的 APP/Web 加解密逆向与流量桥接 | 浏览器 Hook、小程序源码分析、加解密参数还原、Burp 双向加解密桥接和 mitmdump 插件生成 | 面向APP/Web 加解密逆向分析、渗透测试人员的可视化解密框架 | 是 · 2026-07-29 | [3.5](https://github.com/CuriousLearnerDev/CipherBridge/releases/tag/3.5) · 2026-07-27 | 329 |
| [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) | 桌面工作站 | 一体化协议和逆向分析 | 浏览器、代理、Hook、AI 和 MCP 集成 | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE &#124; All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration | 是 · 2026-07-29 | [v3.6.52](https://github.com/Mouseww/anything-analyzer/releases/tag/v3.6.52) · 2026-07-13 | 3404 |
| [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) | 定制浏览器 / Agent | 引擎级 JS、JSVMP 和 WASM 追踪 | 高级混淆、动态代码和底层执行轨迹分析 | 🦊 内置 AI 逆向 Agent 的 Firefox — 通用 JS/JSVMP/WASM/签名逆向工作站，SpiderMonkey 引擎层非侵入 trace，把加密参数从黑盒还原成不依赖浏览器的纯算法 | 是 · 2026-07-29 | [v0.22.4](https://github.com/WhiteNightShadow/firefox-reverse/releases/tag/v0.22.4) · 2026-07-29 | 607 |

## 工具评估维度

| 维度 | 检查重点 |
| --- | --- |
| 工具形态 | MCP、Skill、插件、Agent、桌面应用或知识库；Skill 提供方法，其他形态负责连接或操作工具 |
| 分析能力 | 静态分析、动态分析、流量分析、设备控制、浏览器自动化、代码重建和报告生成 |
| 写操作 | 是否支持重命名、注释、断点、Hook、设备操作或浏览器状态修改；执行前备份分析数据库和测试环境 |
| 上下文占用 | 是否支持按需加载、搜索、摘要、分片读取和最小化返回 |
| 任务产物 | 是否保存请求与响应样本、Hook 脚本、调用链、关键代码、环境依赖、复现代码、失败记录、证据和报告 |
| 部署方式 | 本地桌面、无头服务、Docker、虚拟机、越狱或 Root 设备、浏览器扩展、IDE 插件 |
| 维护情况 | 最近提交、Issue 响应、Release、安装文档、客户端与软件版本、License、实验性功能 |

本列表收录不代表对项目安全性、稳定性或持续维护状态作出保证。

## 使用规范

本项目收录内容仅用于：

* 自有软件和自有系统分析；
* 获得明确授权的安全测试；
* 恶意软件研究；
* 数字取证；
* 互操作性研究；
* 教育和培训；
* CTF；
* 防御性安全研究。

请勿将相关工具用于：

* 未经授权访问他人系统；
* 绕过访问控制或付费限制；
* 窃取账号、凭证、Cookie 或个人数据；
* 批量滥用第三方服务；
* 破坏网站、应用或网络服务；
* 违反软件许可协议、法律法规或平台规则的活动。

使用者应自行确认目标系统的授权范围和所在地法律要求。

## 贡献指南

欢迎提交新的 AI 逆向工程项目。

项目至少满足以下条件之一：

* 提供逆向相关 MCP Server；
* 提供可复用的逆向 Skill；
* 将 AI 集成到逆向软件；
* 提供 AI 驱动的静态或动态分析能力；
* 提供浏览器、设备或抓包工具的 AI 接口；
* 提供完整的逆向 Agent 或工作站。

提交时请包含：

```markdown
| [项目名称](项目地址) | 项目形态 | 一句话核心定位 | 主要适用场景 |
```

可补充说明：

* 支持的平台；
* 安装方式；
* 支持的 AI 客户端；
* 是否需要商业软件；
* 是否需要 Root 或越狱环境；
* License；
* 最近维护时间。

以下项目通常不收录：

* 没有源码或文档的项目；
* 仅有概念介绍、没有可运行实现的项目；
* 长期失效且没有替代价值的项目；
* 主要用于未授权攻击、账号窃取或恶意绕过的工具；
* 与 AI 或逆向工程关系较弱的普通自动化项目。

## Star

如果这份清单对你有帮助，欢迎 Star、Fork 或提交 Pull Request；也欢迎推荐新的 AI 逆向工程工具、MCP、Skill、插件和 Agent。

## License

本列表采用 [MIT License](LICENSE)。

项目列表中的各个工具拥有各自的许可证，使用前请查看对应仓库的 License 和使用说明。
