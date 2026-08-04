<div align="center">

# Awesome AI Reverse Engineering

A curated list of AI-assisted reverse engineering tools, MCP servers, skills, and agents

[简体中文](README.md) | English

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

</div>

## About

Awesome AI Reverse Engineering collects AI-assisted reverse engineering tools for JavaScript and the Web, native binaries, Android and iOS, browser automation, and traffic analysis.

The list includes MCP servers, skills, plugins for IDA Pro, Ghidra, Binary Ninja, and JADX, as well as agents and desktop workstations.

> **Scope of use:** For owned systems, explicitly authorized security testing, digital forensics, education and training, and defensive security research only.

> The GitHub Description column is synchronized verbatim from each upstream repository and may not be in English.

## Tool Types

| Type | Purpose |
| --- | --- |
| MCP Server | Exposes browser, decompiler, debugger, or device capabilities to AI systems |
| Skill | Gives AI systems analysis methods, task procedures, decision criteria, and output conventions |
| IDE / RE Plugin | Integrates AI capabilities into tools such as IDA, Ghidra, JADX, and Binary Ninja |
| Agent | Plans tasks, invokes tools, verifies results, and produces reports based on a goal |
| Desktop Workstation | Combines traffic capture, browser control, hooking, AI analysis, and result management in one application |
| Knowledge Base | Provides vulnerability patterns, cases, and testing ideas without performing analysis directly |

> MCP connects AI systems to analysis tools, skills define analysis methods, and agents handle planning, execution, and verification.

## Contents

- [Quick Selection](#quick-selection)
- [JavaScript and Web Reverse Engineering](#javascript-and-web-reverse-engineering)
- [IDA Pro Ecosystem](#ida-pro-ecosystem)
- [Binary and Native Reverse Engineering](#binary-and-native-reverse-engineering)
- [Ghidra Ecosystem](#ghidra-ecosystem)
- [Android and iOS Security Analysis](#android-and-ios-security-analysis)
- [Browser Automation and Traffic Analysis](#browser-automation-and-traffic-analysis)
- [Evaluation Criteria](#evaluation-criteria)
- [Acceptable Use](#acceptable-use)
- [Contributing](#contributing)

## Quick Selection

| Need | Recommended Project |
| --- | --- |
| Locate common web signatures, parameters, and cookies | [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp) |
| Comprehensive JS, WASM, AST, and network analysis | [jshookmcp](https://github.com/vmoranv/jshookmcp) |
| Advanced Web reversing involving workers, Webpack, or JSVMP | [reverse-skill](https://github.com/715494637/reverse-skill/) |
| Wrap browser encryption functions as APIs | [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) |
| Turn website traffic into reusable API clients | [reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer) |
| Preserve evidence and reproduce algorithms locally | [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP) |
| Use an anti-detection browser environment | [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp) |
| Decrypt WeChat Mini Program packages and recover source trees | [wxapkg](https://github.com/wux1an/wxapkg) |
| Enable F12 debugging for Windows WeChat Mini Programs | [zhong-wechat-wmpf-debugger](https://github.com/netz888/zhong-wechat-wmpf-debugger) |
| Analyze WeChat Mini Program runtimes | [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) |
| Perform real-time AI analysis in IDA Pro | [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) |
| Export IDA data for analysis by an AI coding tool | [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) |
| Run IDA as a headless service | [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) |
| Analyze several IDA instances in parallel | [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) |
| Use multiple AI models directly inside IDA | [WPeGPT](https://github.com/WPeace-HcH/WPeGPT) |
| Use AI with Ghidra in GUI or headless mode | [Ghidra MCP Server](https://github.com/bethington/ghidra-mcp) |
| Connect radare2 to AI agents | [Radare2 MCP Server](https://github.com/radareorg/radare2-mcp) |
| Integrate AI with Binary Ninja | [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) |
| Perform dynamic debugging in x64dbg or x32dbg | [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) |
| Analyze process memory through Cheat Engine | [Cheat Engine MCP Bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge) |
| Automate binary analysis across multiple tools | [revula](https://github.com/president-xd/revula) |
| Extract Android APIs and analyze call chains | [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) |
| Perform interactive AI analysis in JADX | [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) |
| Decode, inspect Smali, and rebuild APKs with Apktool | [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) |
| Reverse Android native SO (.so) libraries | [SOMCP](https://github.com/bilieebiliee1-design/SOMCP) |
| Perform dynamic Android instrumentation with Frida | [frida-analykit](https://github.com/ZSA233/frida-analykit) |
| Connect Charles traffic to AI systems | [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) |
| Use an all-in-one protocol analysis workstation | [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) |
| Trace JS, JSVMP, and WASM at the engine level | [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) |

## JavaScript and Web Reverse Engineering

> Runtime debugging, request-chain tracing, hooking, deobfuscation, WASM, protocol analysis, and local algorithm reproduction for JavaScript.

### General-Purpose MCP Servers

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [jshookmcp](https://github.com/vmoranv/jshookmcp) | MCP | Comprehensive AI-assisted JavaScript security analysis | Browser automation, CDP, network monitoring, JS hooking, WASM, source maps, and AST transformations | js hook toolkit that all you need | Yes · 2026-08-04 | None | 1872 |
| [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp) | MCP | JavaScript debugging in real browser runtimes | Request parameters, dynamic cookies, WebSockets, call chains, and key function tracing | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可选 CloakBrowser。 | Yes · 2026-07-16 | [v4.0.1](https://github.com/zhizhuodemao/js-reverse-mcp/releases/tag/v4.0.1) · 2026-07-10 | 2395 |
| [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP) | MCP / Workflow | Standardized Web reverse engineering workflow | Page inspection, runtime sampling, local reproduction, environment emulation, and evidence preservation | JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它 将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、 Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、 加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等 场景 | Yes · 2026-05-31 | [v2.0.4](https://github.com/NoOne-hub/JSReverser-MCP/releases/tag/v2.0.4) · 2026-05-31 | 958 |

### WeChat Mini Program Reverse Engineering

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [wxapkg](https://github.com/wux1an/wxapkg) | Desktop Tool | WeChat Mini Program package decryption and unpacking | `.wxapkg` scanning, decryption, unpacking, and source-tree recovery | 跨平台微信小程序反编译 GUI 工具，.wxapkg 文件扫描 + 解密 + 解包工具 | No · 2026-04-28 | [v2.0.0](https://github.com/wux1an/wxapkg/releases/tag/v2.0.0) · 2026-04-16 | 3927 |
| [zhong-wechat-wmpf-debugger](https://github.com/netz888/zhong-wechat-wmpf-debugger) | Debugging Tool | F12 debugging for Windows WeChat Mini Programs | WMPF version detection, CDP/DevTools bridging, and legacy or modern runtime debugging | WeChatOpenDevTool 微信小程序强制开启开发者工具 | Yes · 2026-07-18 | [v1.3.0](https://github.com/netz888/zhong-wechat-wmpf-debugger/releases/tag/v1.3.0) · 2026-07-18 | 69 |
| [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) | MCP | CDP debugging for WeChat Mini Programs | WeChat DevTools, desktop WeChat Mini Programs, runtime code, and request analysis | 微信小程序逆向工程 MCP 服务器，让你的 AI 编码助手（如 Claude、Cursor、Antigravity）能够直接通过 Chrome DevTools Protocol (CDP) 调试和分析微信小程序（包括微信开发者工具或 PC 端微信小程序）中的 JavaScript 代码。 | No · 2026-04-22 | None | 130 |

### JavaScript Reverse Engineering Skills

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) | Skill | End-to-end JavaScript reversing with anti-detection browsers | Network capture, source tracing, hooking, algorithm recovery, and local reproduction | 🔧 AI-powered JS逆向工程 Skill —— 覆盖加密还原、混淆分析、动态Cookie、WASM逆向、协议对抗等全链路场景，通过 Node.js 实现算法还原与模拟请求。适配 Claude Code / Claude.ai / 其他AI编码工具 | Yes · 2026-07-29 | [v3.4.1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/releases/tag/v3.4.1) · 2026-07-29 | 971 |
| [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) | Skill | Exposing JavaScript reversing results as services | JSRPC, Flask, autoDecoder, request encryption, and response decryption | 结合chrome-devtools-mcp的能力并加上Skill的规范，实现JSRPC+Flask+autoDecoder方案的前端JS逆向自动化分析，提升JS逆向的效率 | Yes · 2026-07-30 | [v2.1](https://github.com/Fausto-404/js-reverse-automation--skill/releases/tag/v2.1) · 2026-07-28 | 543 |
| [reverse-skill](https://github.com/715494637/reverse-skill/) | Skill | Advanced Web reverse engineering methods | JSVMP, workers, WASM, Webpack, AST, and protocol analysis | 面向 Web JS 逆向分析的技能仓库，覆盖请求链定位、运行时诊断、AST 混淆恢复、JSVMP、worker、WASM、webpack/runtime 与协议语义分析。 | No · 2026-05-02 | [jsr-skills-15-a3e116e](https://github.com/715494637/reverse-skill/releases/tag/jsr-skills-15-a3e116e) · 2026-05-02 | 325 |
| [xbsReverseSkill](https://github.com/lwjjike/xbsReverseSkill) | Skill Suite | Modular Web reverse engineering capabilities | AST analysis, standalone algorithms, protocol analysis, and browser environment emulation | Ai逆向的skill目录 | Yes · 2026-07-21 | [v1.0.0](https://github.com/lwjjike/xbsReverseSkill/releases/tag/v1.0.0) · 2026-03-28 | 342 |

### Specialized Web Security Analysis Tools

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ruishu-mcp](https://github.com/xuange520/ruishu-mcp) | MCP | Dynamic WAF traffic research | Analyzing Ruishu-style dynamic defenses, request parameters, and traffic in authorized environments | 🚀 专为 AI Agent 打造的瑞数防爬流量净化 MCP 工具 / An MCP Tool for AI Agents to Stealthily Bypass and Purify Ruishu WAF Traffic | Yes · 2026-07-13 | [v1.1.0](https://github.com/xuange520/ruishu-mcp/releases/tag/v1.1.0) · 2026-04-13 | 85 |

## IDA Pro Ecosystem

> MCP servers, data-export tools, in-app AI plugins, and multi-instance analysis interfaces for IDA Pro.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) | IDA Plugin / MCP | Direct AI access to and control of IDA Pro | Decompilation, cross-references, renaming, comments, and type recovery | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. | Yes · 2026-08-04 | [1.4.0](https://github.com/mrexodia/ida-pro-mcp/releases/tag/1.4.0) · 2025-10-06 | 11069 |
| [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | IDA Plugin / Export Tool | Exporting IDA data for analysis by AI coding tools | Large-scale code indexing and analysis with low interaction overhead | Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP | Yes · 2026-07-26 | None | 1864 |
| [WPeGPT](https://github.com/WPeace-HcH/WPeGPT) | IDA AI Plugin | Direct integration of multiple AI models into IDA | Interactive binary analysis with models such as OpenAI and DeepSeek | An IDA plugin for binary file analysis, powered by AI models such as OpenAI and DeepSeek. | Yes · 2026-05-27 | [v3.0](https://github.com/WPeace-HcH/WPeGPT/releases/tag/v3.0) · 2026-05-27 | 1396 |
| [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) | MCP | Headless IDA service implemented in Rust | Server deployments and automated pipelines | Headless IDA Pro MCP Server | Yes · 2026-07-27 | [v9.4.1](https://github.com/blacktop/ida-mcp-rs/releases/tag/v9.4.1) · 2026-07-15 | 697 |
| [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) | IDA Plugin / MCP | Managing multiple IDA instances through one endpoint | Parallel multi-binary analysis, cross-sample function similarity, and malware component correlation | Multi-instance IDA Pro MCP server — analyze multiple binaries simultaneously through a single MCP endpoint. | Yes · 2026-07-30 | None | 370 |

## Binary and Native Reverse Engineering

> radare2, Binary Ninja, dynamic debuggers, memory-analysis tools, and cross-tool reverse engineering agents and automation platforms.

### radare2 Ecosystem

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Radare2 MCP Server](https://github.com/radareorg/radare2-mcp) | radare2 Plugin / MCP | Official radare2 interface for AI agents | CLI and remote sessions, headless analysis, read-only mode, sandboxing, and automated pipelines | MCP stdio server for radare2 | Yes · 2026-07-17 | [1.8.4](https://github.com/radareorg/radare2-mcp/releases/tag/1.8.4) · 2026-06-03 | 276 |
| [r2ai](https://github.com/radareorg/r2ai) | radare2 AI Plugin | Local and remote LLMs inside radare2 | Function explanation, automatic naming, vulnerability analysis, decompilation assistance, and ReAct workflows | LLM-based reversing for radare2 | Yes · 2026-07-22 | [1.4.0](https://github.com/radareorg/r2ai/releases/tag/1.4.0) · 2026-06-03 | 462 |

### Dynamic Debugging and Memory Analysis

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cheat Engine MCP Bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge) | Cheat Engine Bridge / MCP | AI-driven process-memory analysis | Memory scans, pointer chains, structure recovery, disassembly, and signature generation | Connect Cursor, Copilot & Claude AI directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language. | Yes · 2026-08-03 | None | 1149 |
| [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) | x64dbg Plugin / MCP | Remote control of x64dbg and x32dbg through MCP | Execution control, breakpoints, memory, registers, disassembly, and automated dynamic debugging | MCP server plugin for x64dbg debugger - enables AI agents and external tools to control debugging via JSON-RPC 2.0 over HTTP/SSE | Yes · 2026-07-18 | [v1.0.10](https://github.com/SetsunaYukiOvO/x64dbg-mcp/releases/tag/v1.0.10) · 2026-07-18 | 343 |

### Other Reverse Engineering Integrations

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Rikugan](https://github.com/buzzer-re/Rikugan) | Agent / Plugin | AI agent embedded in IDA and Binary Ninja | Continuous conversational analysis within a reverse engineering interface | A reverse-engineering agent for IDA Pro and Binary Ninja | Yes · 2026-06-15 | [v1.3.2](https://github.com/buzzer-re/Rikugan/releases/tag/v1.3.2) · 2026-06-15 | 666 |
| [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) | Binary Ninja Plugin / MCP | AI bridge for Binary Ninja | Real-time analysis across multiple binary targets | A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client. | No · 2026-04-05 | [v1.2.1](https://github.com/fosdickio/binary_ninja_mcp/releases/tag/v1.2.1) · 2026-03-22 | 412 |

### General Agents, Platforms, and Knowledge Bases

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | Skill / Router | Routing security tasks and toolchains | Multi-tool orchestration, CTFs, security research, and report generation | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 &#124; 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 | Yes · 2026-08-04 | [v1.0.0](https://github.com/zhaoxuya520/reverse-skill/releases/tag/v1.0.0) · 2026-07-17 | 16994 |
| [Open ReverseLab](https://github.com/LING71671/open-reverselab) | Lab / Knowledge Base / MCP | Agent-native reverse engineering laboratory | Authorized CTF, APK, PE, cryptography, and protocol-analysis workflows | Agent-native reverse-engineering lab with a 197-article knowledge base, MCP tools, and CTF/APK/PE automation workflows. | Yes · 2026-08-01 | [v1.1.0-windows](https://github.com/LING71671/open-reverselab/releases/tag/v1.1.0-windows) · 2026-07-08 | 970 |
| [revula](https://github.com/president-xd/revula) | MCP Platform | General-purpose reverse engineering automation backend | Static analysis, dynamic debugging, malware analysis, and batch processing | A fully functional and production-grade reverse engineering MCP Server | Yes · 2026-07-10 | None | 70 |

## Ghidra Ecosystem

> MCP servers, native extensions, in-app AI plugins, headless automation interfaces, and agents that use Ghidra as their analysis backend.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Ghidra MCP Server](https://github.com/bethington/ghidra-mcp) | Ghidra Plugin / MCP | Comprehensive Ghidra MCP service | GUI and headless analysis, batch operations, P-code, debugging, and team workflows | Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. GUI plugin + headless server, lazy tool loading, convention enforcement, batch operations, Ghidra Server integration, and Docker deployment. | Yes · 2026-08-04 | [v6.0.0](https://github.com/bethington/ghidra-mcp/releases/tag/v6.0.0) · 2026-07-25 | 3135 |
| [auto-re-agent](https://github.com/Dryxio/auto-re-agent) | Agent / Ghidra Backend | Reconstructing and validating C/C++ functions from binaries | Decompilation evidence, candidate source generation, build tests, and parity checks | Open-source AI reverse-engineering agent using Ghidra and LLMs to reconstruct and validate C/C++ functions from binaries. | Yes · 2026-07-23 | [v0.2.1](https://github.com/Dryxio/auto-re-agent/releases/tag/v0.2.1) · 2026-07-23 | 1274 |
| [reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | Ghidra Plugin / MCP | MCP interface for Ghidra reverse engineering tasks | Decompilation, function and data-type analysis, renaming, and comments | MCP server for reverse engineering tasks in Ghidra 👩‍💻 | Yes · 2026-08-04 | [v7.3.0](https://github.com/cyberkaida/reverse-engineering-assistant/releases/tag/v7.3.0) · 2026-06-13 | 796 |
| [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) | Native Ghidra Extension / MCP | An in-process MCP server for Ghidra | Live binary analysis and agent tool calls inside Ghidra | An native MCP server extension for Ghidra | Yes · 2026-08-03 | [2.11.0](https://github.com/symgraph/GhidrAssistMCP/releases/tag/2.11.0) · 2026-08-03 | 695 |
| [GhidraGPT](https://github.com/weirdmachine64/GhidraGPT) | Ghidra AI Plugin | Direct integration of multiple LLMs into Ghidra | Conversational function explanation, symbol naming, and AI-assisted analysis | Integrate LLM models directly into Ghidra for AI-enhanced reverse engineering. | Yes · 2026-07-22 | [v1.4.0](https://github.com/weirdmachine64/GhidraGPT/releases/tag/v1.4.0) · 2026-07-22 | 613 |
| [PyGhidra-MCP](https://github.com/clearbluejar/pyghidra-mcp) | CLI / MCP | Command-line MCP built on PyGhidra | Headless analysis, shared GUI state, scripted tasks, and automated pipelines | Python Command-Line Ghidra MCP | Yes · 2026-08-03 | [v0.2.4](https://github.com/clearbluejar/pyghidra-mcp/releases/tag/v0.2.4) · 2026-08-03 | 397 |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Ghidra Plugin / MCP | Connecting Ghidra to AI clients | Decompilation, function analysis, and symbol organization | MCP Server for Ghidra | No · 2025-06-23 | [1.4](https://github.com/LaurieWired/GhidraMCP/releases/tag/1.4) · 2025-06-23 | 9701 |

## Android and iOS Security Analysis

> APK decompilation, API extraction, dynamic instrumentation, device management, traffic analysis, and mobile security knowledge bases.

### Android Static Analysis and Decompilation

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Skill | Android static analysis and API extraction | APK, XAPK, JAR, AAR, Retrofit, OkHttp, and call-chain analysis | Claude Code skill to support Android app's reverse engineering | Yes · 2026-06-10 | [v1.1.0](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/releases/tag/v1.1.0) · 2026-04-27 | 6675 |
| [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) | JADX Plugin / MCP | Real-time AI analysis in JADX | APK code review, vulnerability analysis, and contextual inspection | Plugin for JADX to integrate MCP server | Yes · 2026-05-28 | [v6.4.0](https://github.com/zinja-coder/jadx-ai-mcp/releases/tag/v6.4.0) · 2026-05-28 | 2597 |
| [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) | Apktool / MCP | AI access to Apktool decoding and rebuilding | Manifest, resource, and Smali analysis; APK decoding, modification, and rebuilding | A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites) | Yes · 2026-07-02 | [V3.0.2](https://github.com/zinja-coder/apktool-mcp-server/releases/tag/V3.0.2) · 2026-07-02 | 616 |
| [SOMCP](https://github.com/bilieebiliee1-design/SOMCP) | Native SO / MCP | On-device Android SO reverse engineering MCP | ELF structure analysis, Rizin disassembly, LIEF ELF patching/rewriting, patch sessions, Cloudflare Tunnel, and APK MCP bridging | Android-native SO reverse engineering MCP server | Yes · 2026-08-04 | [v1.0.17](https://github.com/bilieebiliee1-design/SOMCP/releases/tag/v1.0.17) · 2026-08-03 | 118 |

### Dynamic Instrumentation and Device Control

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [frida-analykit](https://github.com/ZSA233/frida-analykit) | Frida Toolkit / MCP | Dynamic instrumentation for Android agents | Frida version management, low-level tool wrappers, hooks, and runtime analysis | Frida 工具包 - 主要面向安卓端逆向，解决frida环境版本管理和对Agent端常用底层工具方法封装，支持MCP。（目前主要由AI开发维护代码） | Yes · 2026-05-16 | [v2.1.4](https://github.com/ZSA233/frida-analykit/releases/tag/v2.1.4) · 2026-05-14 | 150 |
| [iOS MCP](https://github.com/witchan/ios-mcp) | MCP | Control of jailbroken iOS devices | Applications, files, logs, HID, and accessibility operations | iOS MCP: MCP management tool for jailbroken iPhones, enabling developers and AI agents to inspect and control devices. | Yes · 2026-07-30 | [v1.2.3](https://github.com/witchan/ios-mcp/releases/tag/v1.2.3) · 2026-07-30 | 591 |

## Browser Automation and Traffic Analysis

> Browser control, anti-detection environments, proxy capture, protocol analysis, and all-in-one reverse engineering workstations.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer) | Agent / CLI | Generating typed API clients from endpoints used by websites | Browser traffic capture, endpoint discovery, HAR analysis, and Python/JS/TS client generation | The agent that turns websites into APIs! | Yes · 2026-07-31 | [v0.13.0](https://github.com/kalil0321/reverse-api-engineer/releases/tag/v0.13.0) · 2026-07-27 | 911 |
| [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp) | MCP | Anti-detection and privacy-focused browser automation | Fingerprint controls, proxies, session isolation, and realistic browser environments | No description | Yes · 2026-08-04 | [v2.3.0](https://github.com/whit3rabbit/camoufox-mcp/releases/tag/v2.3.0) · 2026-07-06 | 39 |
| [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) | MCP | AI integration for Charles Proxy | Live traffic, historical sessions, and request analysis | Charles Proxy MCP server for AI agents with live capture, structured traffic analysis, and agent-friendly tool contracts | Yes · 2026-06-23 | [v3.0.3](https://github.com/heizaheiza/Charles-mcp/releases/tag/v3.0.3) · 2026-04-21 | 290 |
| [CipherBridge](https://github.com/CuriousLearnerDev/CipherBridge) | Desktop Workstation / AI Agent | AI-assisted APP/Web encryption reversing and traffic bridging | Browser hooks, Mini Program source analysis, encryption/decryption parameter recovery, bidirectional Burp encryption/decryption bridging, and mitmdump plugin generation | 面向APP/Web 加解密逆向分析、渗透测试人员的可视化解密框架 | Yes · 2026-07-29 | [3.5](https://github.com/CuriousLearnerDev/CipherBridge/releases/tag/3.5) · 2026-07-27 | 331 |
| [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) | Desktop Workstation | All-in-one protocol and reverse engineering analysis | Integrated browser, proxy, hooking, AI, and MCP workflows | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE &#124; All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration | Yes · 2026-08-04 | [v3.6.55](https://github.com/Mouseww/anything-analyzer/releases/tag/v3.6.55) · 2026-08-04 | 3410 |
| [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) | Custom Browser / Agent | Engine-level tracing for JS, JSVMP, and WASM | Advanced obfuscation, dynamic code, and low-level execution tracing | 🦊 内置 AI 逆向 Agent 的 Firefox — 通用 JS/JSVMP/WASM/签名逆向工作站，SpiderMonkey 引擎层非侵入 trace，把加密参数从黑盒还原成不依赖浏览器的纯算法 | Yes · 2026-07-29 | [v0.22.4](https://github.com/WhiteNightShadow/firefox-reverse/releases/tag/v0.22.4) · 2026-07-29 | 612 |

## Evaluation Criteria

| Criterion | What to Check |
| --- | --- |
| Tool type | Whether it is an MCP server, skill, plugin, agent, desktop application, or knowledge base; skills provide methods, while the other types connect to or operate tools |
| Analysis capabilities | Static analysis, dynamic analysis, traffic analysis, device control, browser automation, code reconstruction, and report generation |
| Write operations | Whether it supports renaming, comments, breakpoints, hooking, device actions, or browser state changes; back up analysis databases and test environments before use |
| Context usage | Support for on-demand loading, search, summaries, chunked reading, and minimal responses |
| Deliverables | Whether it preserves request and response samples, hook scripts, call chains, key code, environment dependencies, reproduction code, failure records, evidence, and reports |
| Deployment | Local desktop, headless service, Docker, virtual machine, jailbroken or rooted device, browser extension, or IDE plugin |
| Maintenance | Recent commits, issue responses, releases, installation documentation, supported client and software versions, licenses, and experimental features |

Inclusion in this list does not guarantee a project's security, stability, or continued maintenance.

## Acceptable Use

Projects in this list are intended only for:

* Analysis of software and systems you own;
* Explicitly authorized security testing;
* Malware research;
* Digital forensics;
* Interoperability research;
* Education and training;
* CTF competitions;
* Defensive security research.

Do not use these tools to:

* Access other people's systems without authorization;
* Bypass access controls or paywalls;
* Steal accounts, credentials, cookies, or personal data;
* Abuse third-party services at scale;
* Disrupt websites, applications, or network services;
* Violate software licenses, laws, regulations, or platform rules.

Users are responsible for confirming the authorization scope for the target system and the legal requirements in their jurisdiction.

## Contributing

New AI-assisted reverse engineering projects are welcome.

A project should meet at least one of the following criteria:

* Provide an MCP server for reverse engineering;
* Provide a reusable reverse engineering skill;
* Integrate AI into reverse engineering software;
* Provide AI-assisted static or dynamic analysis;
* Provide an AI interface for browser, device, or traffic-capture tools;
* Provide a complete reverse engineering agent or workstation.

Please include the following when submitting a project:

```markdown
| [Project Name](Project URL) | Project Type | One-Sentence Core Focus | Primary Use Case |
```

You may also include:

* Supported platforms;
* Installation instructions;
* Supported AI clients;
* Whether commercial software is required;
* Whether root access or jailbreaking is required;
* License;
* Most recent maintenance date.

The following projects are generally not included:

* Projects without source code or documentation;
* Concept-only projects without a runnable implementation;
* Long-abandoned projects with no remaining value;
* Tools primarily intended for unauthorized attacks, account theft, or malicious bypasses;
* General automation projects with little connection to AI or reverse engineering.

## Star

If you find this list useful, please star or fork the repository, submit a pull request, or recommend new AI reverse engineering tools, MCP servers, skills, plugins, and agents.

## License

This list is available under the [MIT License](LICENSE).

Each project in the list has its own license. Review the relevant repository's license and usage documentation before use.
