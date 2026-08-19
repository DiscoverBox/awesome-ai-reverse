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
- [Ghidra Ecosystem](#ghidra-ecosystem)
- [Binary and Native Reverse Engineering](#binary-and-native-reverse-engineering)
- [General Agents, Platforms, and Knowledge Bases](#general-agents-platforms-and-knowledge-bases)
- [Android and iOS Security Analysis](#android-and-ios-security-analysis)
- [Browser Automation and Traffic Analysis](#browser-automation-and-traffic-analysis)
- [Watchlist](#watchlist)
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
| Decompile .NET programs | [ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp) |
| Diff IDA binaries and analyze patches | [Diaphora MCP](https://github.com/xTeardx/diaphora-mcp) |
| Recover algorithms from ARM64 traces | [algokiller-plugin](https://github.com/icloudza/algokiller-plugin) |
| Automate binary analysis across multiple tools | [revula](https://github.com/president-xd/revula) |
| Run local agentic reversing with evidence management | [REA](https://github.com/morluto/rea) |
| Combine malware, forensics, and binary analysis | [Reversecore MCP](https://github.com/sjkim1127/Reversecore_MCP) |
| Extract Android APIs and analyze call chains | [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) |
| Perform interactive AI analysis in JADX | [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) |
| Decode, inspect Smali, and rebuild APKs with Apktool | [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) |
| Reverse Android native SO (.so) libraries | [SOMCP](https://github.com/bilieebiliee1-design/SOMCP) |
| Analyze Android DEX, Hermes, and cross-layer taint | [droidsaw](https://github.com/droidsaw/droidsaw) |
| Emulate Android native and Java code off-device | [VortexDBG](https://github.com/carlosadrianosj/VortexDBG) |
| Run full-stack multi-device Android analysis | [FIRERPA](https://github.com/firerpa/lamda) |
| Perform dynamic Android instrumentation with Frida | [frida-analykit](https://github.com/ZSA233/frida-analykit) |
| Connect Charles traffic to AI systems | [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) |
| Inspect, modify, and replay mitmproxy traffic | [mitmproxy-mcp](https://github.com/snapspecter/mitmproxy-mcp) |
| Use an all-in-one protocol analysis workstation | [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) |
| Trace JS, JSVMP, and WASM at the engine level | [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) |

## JavaScript and Web Reverse Engineering

> Runtime debugging, request-chain tracing, hooking, deobfuscation, WASM, protocol analysis, and local algorithm reproduction for JavaScript.

### General-Purpose MCP Servers

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [jshookmcp](https://github.com/vmoranv/jshookmcp) | MCP | Comprehensive AI-assisted JavaScript security analysis | Browser automation, CDP, network monitoring, JS hooking, WASM, source maps, and AST transformations | js hook toolkit that all you need | Yes · 2026-08-04 | None | 1907 |
| [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp) | MCP | JavaScript debugging in real browser runtimes | Request parameters, dynamic cookies, WebSockets, call chains, and key function tracing | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可选 CloakBrowser。 | Yes · 2026-07-16 | [v4.0.1](https://github.com/zhizhuodemao/js-reverse-mcp/releases/tag/v4.0.1) · 2026-07-10 | 2533 |
| [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP) | MCP / Workflow | Standardized Web reverse engineering workflow | Page inspection, runtime sampling, local reproduction, environment emulation, and evidence preservation | JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它 将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、 Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、 加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等 场景 | Yes · 2026-05-31 | [v2.0.4](https://github.com/NoOne-hub/JSReverser-MCP/releases/tag/v2.0.4) · 2026-05-31 | 975 |

### WeChat Mini Program Reverse Engineering

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [wxapkg](https://github.com/wux1an/wxapkg) | Desktop Tool | WeChat Mini Program package decryption and unpacking | `.wxapkg` scanning, decryption, unpacking, and source-tree recovery | 跨平台微信小程序反编译 GUI 工具，.wxapkg 文件扫描 + 解密 + 解包工具 | No · 2026-04-28 | [v2.0.0](https://github.com/wux1an/wxapkg/releases/tag/v2.0.0) · 2026-04-16 | 3986 |
| [zhong-wechat-wmpf-debugger](https://github.com/netz888/zhong-wechat-wmpf-debugger) | Debugging Tool | F12 debugging for Windows WeChat Mini Programs | WMPF version detection, CDP/DevTools bridging, and legacy or modern runtime debugging | WeChatOpenDevTool 微信小程序强制开启开发者工具 | Yes · 2026-07-18 | [v1.3.0](https://github.com/netz888/zhong-wechat-wmpf-debugger/releases/tag/v1.3.0) · 2026-07-18 | 85 |
| [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) | MCP | CDP debugging for WeChat Mini Programs | WeChat DevTools, desktop WeChat Mini Programs, runtime code, and request analysis | 微信小程序逆向工程 MCP 服务器，让你的 AI 编码助手（如 Claude、Cursor、Antigravity）能够直接通过 Chrome DevTools Protocol (CDP) 调试和分析微信小程序（包括微信开发者工具或 PC 端微信小程序）中的 JavaScript 代码。 | No · 2026-04-22 | None | 152 |

### JavaScript Reverse Engineering Skills

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) | Skill | End-to-end JavaScript reversing with anti-detection browsers | Network capture, source tracing, hooking, algorithm recovery, and local reproduction | 🔧 AI-powered JS逆向工程 Skill —— 覆盖加密还原、混淆分析、动态Cookie、WASM逆向、协议对抗等全链路场景，通过 Node.js 实现算法还原与模拟请求。适配 Claude Code / Claude.ai / 其他AI编码工具 | Yes · 2026-07-29 | [v3.4.1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/releases/tag/v3.4.1) · 2026-07-29 | 1094 |
| [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) | Skill | Exposing JavaScript reversing results as services | JSRPC, Flask, autoDecoder, request encryption, and response decryption | 结合chrome-devtools-mcp的能力并加上Skill的规范，实现JSRPC+Flask+autoDecoder方案的前端JS逆向自动化分析，提升JS逆向的效率 | Yes · 2026-07-30 | [v2.1](https://github.com/Fausto-404/js-reverse-automation--skill/releases/tag/v2.1) · 2026-07-28 | 557 |
| [reverse-skill](https://github.com/715494637/reverse-skill/) | Skill | Advanced Web reverse engineering methods | JSVMP, workers, WASM, Webpack, AST, and protocol analysis | 面向 Web JS 逆向分析的技能仓库，覆盖请求链定位、运行时诊断、AST 混淆恢复、JSVMP、worker、WASM、webpack/runtime 与协议语义分析。 | No · 2026-05-02 | [jsr-skills-15-a3e116e](https://github.com/715494637/reverse-skill/releases/tag/jsr-skills-15-a3e116e) · 2026-05-02 | 345 |
| [xbsReverseSkill](https://github.com/lwjjike/xbsReverseSkill) | Skill Suite | Modular Web reverse engineering capabilities | AST analysis, standalone algorithms, protocol analysis, and browser environment emulation | Ai逆向的skill目录 | Yes · 2026-07-21 | [v1.0.0](https://github.com/lwjjike/xbsReverseSkill/releases/tag/v1.0.0) · 2026-03-28 | 354 |

### Custom Browsers and Engine-Level Analysis

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) | Custom Browser / Agent | Engine-level tracing for JS, JSVMP, and WASM | Advanced obfuscation, dynamic code, and low-level execution tracing | 🦊 内置 AI 逆向 Agent 的 Firefox — 通用 JS/JSVMP/WASM/签名逆向工作站，SpiderMonkey 引擎层非侵入 trace，把加密参数从黑盒还原成不依赖浏览器的纯算法 | Yes · 2026-08-14 | [v0.23.0](https://github.com/WhiteNightShadow/firefox-reverse/releases/tag/v0.23.0) · 2026-08-14 | 687 |

### Specialized Web Security Analysis Tools

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ruishu-mcp](https://github.com/xuange520/ruishu-mcp) | MCP | Dynamic WAF traffic research | Analyzing Ruishu-style dynamic defenses, request parameters, and traffic in authorized environments | 🚀 专为 AI Agent 打造的瑞数防爬流量净化 MCP 工具 / An MCP Tool for AI Agents to Stealthily Bypass and Purify Ruishu WAF Traffic | Yes · 2026-07-13 | [v1.1.0](https://github.com/xuange520/ruishu-mcp/releases/tag/v1.1.0) · 2026-04-13 | 86 |

## IDA Pro Ecosystem

> MCP servers, data-export tools, in-app AI plugins, and multi-instance analysis interfaces for IDA Pro.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) | IDA Plugin / MCP | Direct AI access to and control of IDA Pro | Decompilation, cross-references, renaming, comments, and type recovery | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. | Yes · 2026-08-17 | [1.4.0](https://github.com/mrexodia/ida-pro-mcp/releases/tag/1.4.0) · 2025-10-06 | 11431 |
| [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | IDA Plugin / Export Tool | Exporting IDA data for analysis by AI coding tools | Large-scale code indexing and analysis with low interaction overhead | Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP | Yes · 2026-07-26 | None | 1922 |
| [WPeGPT](https://github.com/WPeace-HcH/WPeGPT) | IDA AI Plugin | Direct integration of multiple AI models into IDA | Interactive binary analysis with models such as OpenAI and DeepSeek | An IDA plugin for binary file analysis, powered by AI models such as OpenAI and DeepSeek. | Yes · 2026-05-27 | [v3.0](https://github.com/WPeace-HcH/WPeGPT/releases/tag/v3.0) · 2026-05-27 | 1412 |
| [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) | MCP | Headless IDA service implemented in Rust | Server deployments and automated pipelines | Headless IDA Pro MCP Server | Yes · 2026-08-17 | [v9.4.2](https://github.com/blacktop/ida-mcp-rs/releases/tag/v9.4.2) · 2026-08-15 | 740 |
| [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) | IDA Plugin / MCP | Managing multiple IDA instances through one endpoint | Parallel multi-binary analysis, cross-sample function similarity, and malware component correlation | Multi-instance IDA Pro MCP server — analyze multiple binaries simultaneously through a single MCP endpoint. | Yes · 2026-07-30 | None | 391 |

## Ghidra Ecosystem

> MCP servers, native extensions, in-app AI plugins, headless automation interfaces, and agents that use Ghidra as their analysis backend.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Ghidra MCP Server](https://github.com/bethington/ghidra-mcp) | Ghidra Plugin / MCP | Comprehensive Ghidra MCP service | GUI and headless analysis, batch operations, P-code, debugging, and team workflows | Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. GUI plugin + headless server, lazy tool loading, convention enforcement, batch operations, Ghidra Server integration, and Docker deployment. | Yes · 2026-08-14 | [v6.0.0](https://github.com/bethington/ghidra-mcp/releases/tag/v6.0.0) · 2026-07-25 | 3355 |
| [auto-re-agent](https://github.com/Dryxio/auto-re-agent) | Agent / Ghidra Backend | Reconstructing and validating C/C++ functions from binaries | Decompilation evidence, candidate source generation, build tests, and parity checks | Open-source AI reverse-engineering agent using Ghidra and LLMs to reconstruct and validate C/C++ functions from binaries. | Yes · 2026-07-23 | [v0.2.1](https://github.com/Dryxio/auto-re-agent/releases/tag/v0.2.1) · 2026-07-23 | 1362 |
| [reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | Ghidra Plugin / MCP | MCP interface for Ghidra reverse engineering tasks | Decompilation, function and data-type analysis, renaming, and comments | MCP server for reverse engineering tasks in Ghidra 👩‍💻 | Yes · 2026-08-18 | [v7.3.0](https://github.com/cyberkaida/reverse-engineering-assistant/releases/tag/v7.3.0) · 2026-06-13 | 806 |
| [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) | Native Ghidra Extension / MCP | An in-process MCP server for Ghidra | Live binary analysis and agent tool calls inside Ghidra | An native MCP server extension for Ghidra | Yes · 2026-08-03 | [2.11.0](https://github.com/symgraph/GhidrAssistMCP/releases/tag/2.11.0) · 2026-08-03 | 722 |
| [GhidraGPT](https://github.com/weirdmachine64/GhidraGPT) | Ghidra AI Plugin | Direct integration of multiple LLMs into Ghidra | Conversational function explanation, symbol naming, and AI-assisted analysis | Integrate LLM models directly into Ghidra for AI-enhanced reverse engineering. | Yes · 2026-07-22 | [v1.4.0](https://github.com/weirdmachine64/GhidraGPT/releases/tag/v1.4.0) · 2026-07-22 | 662 |
| [PyGhidra-MCP](https://github.com/clearbluejar/pyghidra-mcp) | CLI / MCP | Command-line MCP built on PyGhidra | Headless analysis, shared GUI state, scripted tasks, and automated pipelines | Python Command-Line Ghidra MCP | Yes · 2026-08-09 | [v0.2.5](https://github.com/clearbluejar/pyghidra-mcp/releases/tag/v0.2.5) · 2026-08-06 | 412 |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Ghidra Plugin / MCP | Connecting Ghidra to AI clients | Decompilation, function analysis, and symbol organization | MCP Server for Ghidra | No · 2025-06-23 | [1.4](https://github.com/LaurieWired/GhidraMCP/releases/tag/1.4) · 2025-06-23 | 9819 |

## Binary and Native Reverse Engineering

> radare2, Binary Ninja, dynamic debuggers, memory-analysis tools, and cross-tool reverse engineering agents.

### radare2 Ecosystem

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Radare2 MCP Server](https://github.com/radareorg/radare2-mcp) | radare2 Plugin / MCP | Official radare2 interface for AI agents | CLI and remote sessions, headless analysis, read-only mode, sandboxing, and automated pipelines | MCP stdio server for radare2 | Yes · 2026-08-16 | [1.8.6](https://github.com/radareorg/radare2-mcp/releases/tag/1.8.6) · 2026-08-06 | 292 |
| [r2ai](https://github.com/radareorg/r2ai) | radare2 AI Plugin | Local and remote LLMs inside radare2 | Function explanation, automatic naming, vulnerability analysis, decompilation assistance, and ReAct workflows | LLM-based reversing for radare2 | Yes · 2026-08-18 | [1.4.2](https://github.com/radareorg/r2ai/releases/tag/1.4.2) · 2026-08-16 | 466 |

### .NET and Binary Diffing

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp) | .NET Decompiler / MCP | Managed-assembly analysis built on ILSpy | Type discovery, structural analysis, and method-level decompilation for `.dll` and `.exe` files | 🔓 UNLEASH ILSpy'S POWER. Reverse-engineer DOTNET code at GOD SPEED. AI-assisted debugging that THINKS with you. Decompile ANYTHING. 🚀 | Yes · 2026-08-10 | [v1.0.3](https://github.com/bivex/ILSpy-Mcp/releases/tag/v1.0.3) · 2026-08-06 | 54 |
| [Diaphora MCP](https://github.com/xTeardx/diaphora-mcp) | IDA / Diaphora / MCP | Automated binary diffing | IDA database export, function matching, call-graph changes, security triage, and patch reports | MCP server for automated binary diffing. | Yes · 2026-07-15 | [v1.0.6](https://github.com/xTeardx/diaphora-mcp/releases/tag/v1.0.6) · 2026-07-15 | 17 |

### Dynamic Debugging and Memory Analysis

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cheat Engine MCP Bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge) | Cheat Engine Bridge / MCP | AI-driven process-memory analysis | Memory scans, pointer chains, structure recovery, disassembly, and signature generation | Connect Cursor, Copilot & Claude AI directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language. | Yes · 2026-08-14 | None | 1260 |
| [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) | x64dbg Plugin / MCP | Remote control of x64dbg and x32dbg through MCP | Execution control, breakpoints, memory, registers, disassembly, and automated dynamic debugging | MCP server plugin for x64dbg debugger - enables AI agents and external tools to control debugging via JSON-RPC 2.0 over HTTP/SSE | Yes · 2026-08-09 | [v1.0.10](https://github.com/SetsunaYukiOvO/x64dbg-mcp/releases/tag/v1.0.10) · 2026-07-18 | 395 |
| [algokiller-plugin](https://github.com/icloudza/algokiller-plugin) | Plugin / Skill / MCP | ARM64 execution-trace evidence analysis | Searching GB-scale traces, locating critical data flows, and recovering cryptographic algorithms | ARM64 trace evidence analysis & cipher algorithm recovery — Claude Desktop plugin with skills + local MCP server driving the native ak_search engine over GB-scale trace files | No · 2026-05-14 | None | 77 |

### Other Reverse Engineering Integrations

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Rikugan](https://github.com/buzzer-re/Rikugan) | Agent / Plugin | AI agent embedded in IDA and Binary Ninja | Continuous conversational analysis within a reverse engineering interface | A reverse-engineering agent for IDA Pro and Binary Ninja | Yes · 2026-06-15 | [v1.3.2](https://github.com/buzzer-re/Rikugan/releases/tag/v1.3.2) · 2026-06-15 | 669 |
| [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) | Binary Ninja Plugin / MCP | AI bridge for Binary Ninja | Real-time analysis across multiple binary targets | A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client. | No · 2026-04-05 | [v1.2.1](https://github.com/fosdickio/binary_ninja_mcp/releases/tag/v1.2.1) · 2026-03-22 | 423 |

## General Agents, Platforms, and Knowledge Bases

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | Skill / Router | Routing security tasks and toolchains | Multi-tool orchestration, CTFs, security research, and report generation | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 &#124; 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 | Yes · 2026-08-19 | [v1.0.1](https://github.com/zhaoxuya520/reverse-skill/releases/tag/v1.0.1) · 2026-08-08 | 26405 |
| [Open ReverseLab](https://github.com/LING71671/open-reverselab) | Lab / Knowledge Base / MCP | Agent-native reverse engineering laboratory | Authorized CTF, APK, PE, cryptography, and protocol-analysis workflows | Agent-native reverse-engineering lab with a 197-article knowledge base, MCP tools, and CTF/APK/PE automation workflows. | Yes · 2026-08-12 | [v1.1.0-windows](https://github.com/LING71671/open-reverselab/releases/tag/v1.1.0-windows) · 2026-07-08 | 1071 |
| [revula](https://github.com/president-xd/revula) | MCP Platform | General-purpose reverse engineering automation backend | Static analysis, dynamic debugging, malware analysis, and batch processing | A fully functional and production-grade reverse engineering MCP Server | Yes · 2026-08-16 | None | 72 |
| [REA](https://github.com/morluto/rea) | Agent / CLI / MCP / Skill | Local agentic reverse engineering investigation platform | Application behavior and native binary analysis, structured evidence, version comparison, and feature reconstruction | Reverse engineer anything with agents, from app behavior down to native binaries. | Yes · 2026-08-14 | [rea-agents-3.1.0](https://github.com/morluto/rea/releases/tag/rea-agents-3.1.0) · 2026-08-09 | 351 |
| [Reversecore MCP](https://github.com/sjkim1127/Reversecore_MCP) | MCP Platform | Multi-tool security and reverse engineering interface | Orchestrating and reporting across radare2, YARA, LIEF, CAPA, angr, Volatility, and related tools | A security-first MCP server that empowers AI agents to perform automated reverse engineering, malware analysis, forensics, vulnerability research, and SAST — powered by Radare2, YARA, LIEF, Capstone, and more. | Yes · 2026-08-18 | [v3.0.3](https://github.com/sjkim1127/Reversecore_MCP/releases/tag/v3.0.3) · 2026-08-13 | 187 |

## Android and iOS Security Analysis

> APK decompilation, API extraction, dynamic instrumentation, device management, traffic analysis, and mobile security knowledge bases.

### Android Static Analysis and Decompilation

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Skill | Android static analysis and API extraction | APK, XAPK, JAR, AAR, Retrofit, OkHttp, and call-chain analysis | Claude Code skill to support Android app's reverse engineering | Yes · 2026-06-10 | [v1.1.0](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/releases/tag/v1.1.0) · 2026-04-27 | 6830 |
| [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) | JADX Plugin / MCP | Real-time AI analysis in JADX | APK code review, vulnerability analysis, and contextual inspection | Plugin for JADX to integrate MCP server | Yes · 2026-08-06 | [V6.4.1](https://github.com/zinja-coder/jadx-ai-mcp/releases/tag/V6.4.1) · 2026-08-06 | 2676 |
| [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) | Apktool / MCP | AI access to Apktool decoding and rebuilding | Manifest, resource, and Smali analysis; APK decoding, modification, and rebuilding | A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites) | Yes · 2026-07-02 | [V3.0.2](https://github.com/zinja-coder/apktool-mcp-server/releases/tag/V3.0.2) · 2026-07-02 | 632 |
| [SOMCP](https://github.com/bilieebiliee1-design/SOMCP) | Native SO / MCP | On-device Android SO reverse engineering MCP | ELF structure analysis, Rizin disassembly, LIEF ELF patching/rewriting, patch sessions, Cloudflare Tunnel, and APK MCP bridging | SOMCP 是一个运行在 Android 手机上的本地 SO 逆向 MCP 服务器。它通过 Streamable HTTP 暴露 MCP 工具，让客户端可以在手机上完成 ELF 结构分析、Rizin 反汇编/分析、LIEF ELF 修复/重写、补丁会话、构建导出、Cloudflare Tunnel 暴露和可选 APK MCP 桥接 | Yes · 2026-08-19 | [v1.0.17](https://github.com/bilieebiliee1-design/SOMCP/releases/tag/v1.0.17) · 2026-08-17 | 139 |
| [droidsaw](https://github.com/droidsaw/droidsaw) | Android Decompiler / MCP | DEX, Hermes, and React Native cross-layer analysis | DEX-to-Java, Hermes-to-JavaScript, cross-bridge taint analysis, SBOM generation, and auditing | Pure-Rust Android decompiler and security-audit suite. DEX → Java, Hermes → JavaScript. Cross-layer taint across the React Native bridge. CycloneDX SBOM + OpenVEX. CLI and MCP. Bytecode is not a security layer. | Yes · 2026-06-11 | None | 27 |

### Dynamic Instrumentation and Device Control

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [FIRERPA](https://github.com/firerpa/lamda) | Android Platform / MCP / Agent | Full-stack Android device control and dynamic analysis | Multi-device remote control, UI/OCR automation, MITM, Frida, proxy networking, and long-running tasks | Android Full-Stack Device Control Platform: WebRTC/H.264 remote desktop, UI/OCR/image-matching automation, one-click MITM, built-in Frida, proxy/VPN/frp/P2P networking, MCP/Agent, 160+ APIs, designed for multi-device clusters and engineered deployments. | Yes · 2026-08-16 | [v10.6](https://github.com/firerpa/lamda/releases/tag/v10.6) · 2026-08-16 | 8197 |
| [VortexDBG](https://github.com/carlosadrianosj/VortexDBG) | Android Emulator / MCP | Off-device combined native and DEX/Java emulation | ARM `.so`, Dalvik/Java, JNI, breakpoints, memory, registers, and call tracing | Emulate Android native libraries and DEX/Java classes together, off-device, and drive them with AI through MCP. A production-grade Kotlin engine for Android reverse engineering: native .so emulation (Unicorn2, Dynarmic), Dalvik/DEX and JNI, off-device automation. 安卓逆向工程引擎：在同一处同时模拟原生库与 DEX/Java 类，脱机运行，并通过 MCP 用 AI 驱动。Kotlin 打造，面向生产。 | Yes · 2026-07-16 | None | 9 |
| [frida-analykit](https://github.com/ZSA233/frida-analykit) | Frida Toolkit / MCP | Dynamic instrumentation for Android agents | Frida version management, low-level tool wrappers, hooks, and runtime analysis | Frida 工具包 - 主要面向安卓端逆向，解决frida环境版本管理和对Agent端常用底层工具方法封装，支持MCP。（目前主要由AI开发维护代码） | No · 2026-05-16 | [v2.1.4](https://github.com/ZSA233/frida-analykit/releases/tag/v2.1.4) · 2026-05-14 | 153 |
| [iOS MCP](https://github.com/witchan/ios-mcp) | MCP | Control of jailbroken iOS devices | Applications, files, logs, HID, and accessibility operations | iOS MCP: MCP management tool for jailbroken iPhones, enabling developers and AI agents to inspect and control devices. | Yes · 2026-07-30 | [v1.2.3](https://github.com/witchan/ios-mcp/releases/tag/v1.2.3) · 2026-07-30 | 608 |

## Browser Automation and Traffic Analysis

> Browser control, anti-detection environments, proxy capture, protocol analysis, and all-in-one reverse engineering workstations.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [reverse-api-engineer](https://github.com/nottelabs/reverse-api-engineer) | Agent / CLI | Generating typed API clients from endpoints used by websites | Browser traffic capture, endpoint discovery, HAR analysis, and Python/JS/TS client generation | The agent that turns websites into APIs! | Yes · 2026-08-18 | [v0.13.0](https://github.com/nottelabs/reverse-api-engineer/releases/tag/v0.13.0) · 2026-07-27 | 995 |
| [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp) | MCP | Anti-detection and privacy-focused browser automation | Fingerprint controls, proxies, session isolation, and realistic browser environments | No description | Yes · 2026-08-08 | [v2.5.0](https://github.com/whit3rabbit/camoufox-mcp/releases/tag/v2.5.0) · 2026-08-08 | 40 |
| [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) | MCP | AI integration for Charles Proxy | Live traffic, historical sessions, and request analysis | Charles Proxy MCP server for AI agents with live capture, structured traffic analysis, and agent-friendly tool contracts | Yes · 2026-06-23 | [v3.0.3](https://github.com/heizaheiza/Charles-mcp/releases/tag/v3.0.3) · 2026-04-21 | 295 |
| [mitmproxy-mcp](https://github.com/snapspecter/mitmproxy-mcp) | mitmproxy / MCP | AI-driven HTTP/HTTPS traffic operations | Traffic search, interception, modification, replay, authentication discovery, and API-structure extraction | MCP Server that wraps mitmproxy and exposes it as a tool to any MCP client, allows your AI agents to inspect traffic, filter traffic, intercept & modify traffic, request reply, set global headers, and start/stop mitmproxy as needed. | Yes · 2026-06-05 | [v0.6.1](https://github.com/snapspecter/mitmproxy-mcp/releases/tag/v0.6.1) · 2026-06-04 | 105 |
| [CipherBridge](https://github.com/CuriousLearnerDev/CipherBridge) | Desktop Workstation / AI Agent | AI-assisted APP/Web encryption reversing and traffic bridging | Browser hooks, Mini Program source analysis, encryption/decryption parameter recovery, bidirectional Burp encryption/decryption bridging, and mitmdump plugin generation | 面向APP/Web 加解密逆向分析、渗透测试人员的可视化解密框架 | Yes · 2026-08-09 | [3.5](https://github.com/CuriousLearnerDev/CipherBridge/releases/tag/3.5) · 2026-07-27 | 361 |
| [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) | Desktop Workstation | All-in-one protocol and reverse engineering analysis | Integrated browser, proxy, hooking, AI, and MCP workflows | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE &#124; All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration | Yes · 2026-08-07 | [v3.6.60](https://github.com/Mouseww/anything-analyzer/releases/tag/v3.6.60) · 2026-08-07 | 3539 |

## Watchlist

> These projects closely match the scope of this list, but their maintenance continuity, maturity, licensing, or overlap with existing entries still merits observation. Watchlist placement does not mean they should not be tested.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release | Stars |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [WinDbg MCP](https://github.com/memoryforensics1/windbg-mcp) | WinDbg / MCP | Windows kernel and user-mode debugging interface | DbgEng, KDNET, TTD, Frida, remote debugging, and virtual-machine control | C# MCP server for kernel & user-mode Windows debugging — DbgEng COM, KDNET, Frida, dbgsrv, TTD, and integrated VM control. 29 tools for LLM agents. | Yes · 2026-07-05 | None | 39 |
| [HexGraph](https://github.com/branover/hexgraph) | Local Workstation / Agent / MCP | Binary and firmware vulnerability research workbench | Decompilation, fuzzing, verification, evidence graphs, and research notes | Self-hosted, agentic vulnerability research for binaries & firmware: an AI agent decompiles, fuzzes, and verifies exploits inside a sandbox, recording every finding to a typed graph. BYOK, fully local. | Yes · 2026-08-15 | [hexgraph-v0.9.0](https://github.com/branover/hexgraph/releases/tag/hexgraph-v0.9.0) · 2026-07-07 | 19 |
| [jebmcp](https://github.com/flankerhqd/jebmcp) | JEB Pro Plugin / MCP | AI-client access to JEB Pro analysis | APK decompilation, call relationships, manifests, symbol renaming, and vulnerability analysis | No description | No · 2026-04-26 | None | 257 |
| [OGhidra](https://github.com/llnl/OGhidra) | Ghidra Plugin / Agent | Local or cloud LLM analysis inside Ghidra | Natural-language queries, automatic renaming, knowledge graphs, malware patterns, and multi-instance analysis | OGhidra bridges Large Language Models (LLMs) via Ollama with the Ghidra reverse engineering platform, enabling AI-driven binary analysis through natural language. Interact with Ghidra using conversational queries and automate complex reverse engineering workflows. | Yes · 2026-08-17 | None | 414 |

Reasons for watchlist placement:

* WinDbg MCP currently has a short commit history, so real-world compatibility and maintenance continuity need more evidence;
* HexGraph is still early, extends into exploit verification, and uses AGPL-3.0;
* jebmcp describes itself as a quick implementation and does not currently declare a clear repository license;
* OGhidra is substantial, but overlaps with several Ghidra MCP servers and agents already listed.

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
