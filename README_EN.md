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
- [Binary and Native Reverse Engineering](#binary-and-native-reverse-engineering)
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
| Analyze WeChat Mini Program runtimes | [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) |
| Perform real-time AI analysis in IDA Pro | [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) |
| Export IDA data for analysis by an AI coding tool | [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) |
| Run IDA as a headless service | [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) |
| Integrate AI with Ghidra | [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) |
| Integrate AI with Binary Ninja | [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) |
| Perform dynamic debugging in x64dbg or x32dbg | [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) |
| Automate binary analysis across multiple tools | [revula](https://github.com/president-xd/revula) |
| Extract Android APIs and analyze call chains | [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) |
| Perform interactive AI analysis in JADX | [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) |
| Dynamically hook Android applications | [Frida MCP Server](https://github.com/zhizhuodemao/frida-mcp) |
| Automate Android devices | [ADB MCP Server](https://github.com/zhizhuodemao/adb-mcp) |
| Capture and query Android traffic | [Android Proxy MCP](https://github.com/zhizhuodemao/android_proxy_mcp) |
| Connect Charles traffic to AI systems | [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) |
| Use an all-in-one protocol analysis workstation | [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) |
| Trace JS, JSVMP, and WASM at the engine level | [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) |

## JavaScript and Web Reverse Engineering

> Runtime debugging, request-chain tracing, hooking, deobfuscation, WASM, protocol analysis, and local algorithm reproduction for JavaScript.

### General-Purpose MCP Servers

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |
| --- | --- | --- | --- | --- | --- | --- |
| [jshookmcp](https://github.com/vmoranv/jshookmcp) | MCP | Comprehensive AI-assisted JavaScript security analysis | Browser automation, CDP, network monitoring, JS hooking, WASM, source maps, and AST transformations | js hook toolkit that all you need | Yes · 2026-07-13 | None |
| [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp) | MCP | JavaScript debugging in real browser runtimes | Request parameters, dynamic cookies, WebSockets, call chains, and key function tracing | AI Agent-first JS 逆向 MCP Server：有头 Chrome 调试、断点、网络/WebSocket 分析、Patchright 反检测，可选 CloakBrowser。 | Yes · 2026-07-10 | [v4.0.1](https://github.com/zhizhuodemao/js-reverse-mcp/releases/tag/v4.0.1) · 2026-07-10 |
| [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP) | MCP / Workflow | Standardized Web reverse engineering workflow | Page inspection, runtime sampling, local reproduction, environment emulation, and evidence preservation | JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它 将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、 Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、 加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等 场景 | Yes · 2026-05-31 | [v2.0.4](https://github.com/NoOne-hub/JSReverser-MCP/releases/tag/v2.0.4) · 2026-05-31 |
| [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) | MCP | CDP debugging for WeChat Mini Programs | WeChat DevTools, desktop WeChat Mini Programs, runtime code, and request analysis | 微信小程序逆向工程 MCP 服务器，让你的 AI 编码助手（如 Claude、Cursor、Antigravity）能够直接通过 Chrome DevTools Protocol (CDP) 调试和分析微信小程序（包括微信开发者工具或 PC 端微信小程序）中的 JavaScript 代码。 | Yes · 2026-04-22 | None |

### JavaScript Reverse Engineering Skills

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |
| --- | --- | --- | --- | --- | --- | --- |
| [hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) | Skill | End-to-end JavaScript reversing with anti-detection browsers | Network capture, source tracing, hooking, algorithm recovery, and local reproduction | 🔧 AI-powered JS逆向工程 Skill —— 覆盖加密还原、混淆分析、动态Cookie、WASM逆向、协议对抗等全链路场景，通过 Node.js 实现算法还原与模拟请求。适配 Claude Code / Claude.ai / 其他AI编码工具 | Yes · 2026-04-23 | [v3.2.0](https://github.com/WhiteNightShadow/hello_js_reverse_skill/releases/tag/v3.2.0) · 2026-04-18 |
| [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) | Skill | Exposing JavaScript reversing results as services | JSRPC, Flask, autoDecoder, request encryption, and response decryption | 结合chrome-devtools-mcp的能力并加上Skill的规范，实现JSRPC+Flask+autoDecoder方案的前端JS逆向自动化分析，提升JS逆向的效率 | Yes · 2026-06-02 | [v2.0](https://github.com/Fausto-404/js-reverse-automation--skill/releases/tag/v2.0) · 2026-05-31 |
| [JSHook Reverse Tool](https://github.com/wuji66dde/jshook-skill) | Skill / Tool | Code collection, deobfuscation, and hooking support | Large-script collection, cryptography detection, CDP, and incremental analysis | AI-powered JS reverse engineering: deobfuscation, crypto detection, CDP debugging, hook injection, anti-detection &#124; AI驱动JS逆向：反混淆、加密识别、CDP调试、Hook注入、反检测 | No · 2026-02-11 | None |
| [reverse-skill](https://github.com/715494637/reverse-skill/) | Skill | Advanced Web reverse engineering methods | JSVMP, workers, WASM, Webpack, AST, and protocol analysis | 面向 Web JS 逆向分析的技能仓库，覆盖请求链定位、运行时诊断、AST 混淆恢复、JSVMP、worker、WASM、webpack/runtime 与协议语义分析。 | Yes · 2026-05-02 | [jsr-skills-15-a3e116e](https://github.com/715494637/reverse-skill/releases/tag/jsr-skills-15-a3e116e) · 2026-05-02 |
| [xbsReverseSkill](https://github.com/lwjjike/xbsReverseSkill) | Skill Suite | Modular Web reverse engineering capabilities | AST analysis, standalone algorithms, protocol analysis, and browser environment emulation | Ai逆向的skill目录 | Yes · 2026-07-11 | [v1.0.0](https://github.com/lwjjike/xbsReverseSkill/releases/tag/v1.0.0) · 2026-03-28 |

### Specialized Web Security Analysis Tools

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |
| --- | --- | --- | --- | --- | --- | --- |
| [ruishu-mcp](https://github.com/xuange520/ruishu-mcp) | MCP | Dynamic WAF traffic research | Analyzing Ruishu-style dynamic defenses, request parameters, and traffic in authorized environments | 🚀 专为 AI Agent 打造的瑞数防爬流量净化 MCP 工具 / An MCP Tool for AI Agents to Stealthily Bypass and Purify Ruishu WAF Traffic | Yes · 2026-07-13 | [v1.1.0](https://github.com/xuange520/ruishu-mcp/releases/tag/v1.1.0) · 2026-04-13 |

## Binary and Native Reverse Engineering

> IDA Pro, Ghidra, Binary Ninja, debuggers, disassemblers, and automated binary analysis.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |
| --- | --- | --- | --- | --- | --- | --- |
| [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | IDA Plugin / Export Tool | Exporting IDA data for analysis by AI coding tools | Large-scale code indexing and analysis with low interaction overhead | Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP | Yes · 2026-06-15 | None |
| [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) | MCP | Direct AI access to and control of IDA Pro | Decompilation, cross-references, renaming, comments, and type recovery | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. | Yes · 2026-06-22 | [1.4.0](https://github.com/mrexodia/ida-pro-mcp/releases/tag/1.4.0) · 2025-10-06 |
| [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) | MCP | Headless IDA service implemented in Rust | Server deployments and automated pipelines | Headless IDA Pro MCP Server | Yes · 2026-07-09 | [v9.3.26](https://github.com/blacktop/ida-mcp-rs/releases/tag/v9.3.26) · 2026-07-08 |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Ghidra Plugin / MCP | Connecting Ghidra to AI clients | Decompilation, function analysis, and symbol organization | MCP Server for Ghidra | No · 2025-06-23 | [1.4](https://github.com/LaurieWired/GhidraMCP/releases/tag/1.4) · 2025-06-23 |
| [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) | Plugin / MCP | AI bridge for Binary Ninja | Real-time analysis across multiple binary targets | A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client. | No · 2026-04-05 | [v1.2.1](https://github.com/fosdickio/binary_ninja_mcp/releases/tag/v1.2.1) · 2026-03-22 |
| [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) | Plugin / MCP | Remote control of x64dbg and x32dbg through MCP | Execution control, breakpoints, memory, registers, disassembly, and automated dynamic debugging | MCP server plugin for x64dbg debugger - enables AI agents and external tools to control debugging via JSON-RPC 2.0 over HTTP/SSE | Yes · 2026-07-13 | [v1.0.9](https://github.com/SetsunaYukiOvO/x64dbg-mcp/releases/tag/v1.0.9) · 2026-07-13 |
| [revula](https://github.com/president-xd/revula) | MCP Platform | General-purpose reverse engineering automation backend | Static analysis, dynamic debugging, malware analysis, and batch processing | A fully functional and production-grade reverse engineering MCP Server | Yes · 2026-07-10 | None |
| [Rikugan](https://github.com/buzzer-re/Rikugan) | Agent / Plugin | AI agent embedded in IDA and Binary Ninja | Continuous conversational analysis within a reverse engineering interface | A reverse-engineering agent for IDA Pro and Binary Ninja | Yes · 2026-06-15 | [v1.3.2](https://github.com/buzzer-re/Rikugan/releases/tag/v1.3.2) · 2026-06-15 |
| [reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | Skill / Router | Routing security tasks and toolchains | Multi-tool orchestration, CTFs, security research, and report generation | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 &#124; 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 | Yes · 2026-07-10 | None |

## Android and iOS Security Analysis

> APK decompilation, API extraction, dynamic instrumentation, device management, traffic analysis, and mobile security knowledge bases.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |
| --- | --- | --- | --- | --- | --- | --- |
| [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Skill | Android static analysis and API extraction | APK, XAPK, JAR, AAR, Retrofit, OkHttp, and call-chain analysis | Claude Code skill to support Android app's reverse engineering | Yes · 2026-06-10 | [v1.1.0](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/releases/tag/v1.1.0) · 2026-04-27 |
| [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp) | JADX Plugin / MCP | Real-time AI analysis in JADX | APK code review, vulnerability analysis, and contextual inspection | Plugin for JADX to integrate MCP server | Yes · 2026-05-28 | [v6.4.0](https://github.com/zinja-coder/jadx-ai-mcp/releases/tag/v6.4.0) · 2026-05-28 |
| [Frida MCP Server](https://github.com/zhizhuodemao/frida-mcp) | MCP | Dynamic Android instrumentation | Java and native hooking, plus argument and return-value collection | 一个用于frida动态调试的mcp工具，支持自定义frida路径和名称端口,自动管理frida | No · 2025-11-04 | None |
| [Android Proxy MCP](https://github.com/zhizhuodemao/android_proxy_mcp) | MCP | Android traffic capture and querying | Filtering, searching, and analyzing HTTP and HTTPS requests | 基于 MCP 的 Android 抓包服务，让 AI 助手通过自然语言分析网络请求。 | No · 2026-02-09 | None |
| [ADB MCP Server](https://github.com/zhizhuodemao/adb-mcp) | MCP | Android device automation | Installation, launching, screenshots, recordings, files, and Logcat | 安卓adb的mcp命令 | No · 2025-08-25 | None |
| [iOS MCP](https://github.com/witchan/ios-mcp) | MCP | Control of jailbroken iOS devices | Applications, files, logs, HID, and accessibility operations | iOS MCP: MCP management tool for jailbroken iPhones, enabling developers and AI agents to inspect and control devices. | Yes · 2026-07-09 | [v1.2.2](https://github.com/witchan/ios-mcp/releases/tag/v1.2.2) · 2026-07-09 |
| [android-h1](https://github.com/s7safe/android-h1) | Skill / Knowledge Base | Mobile security vulnerability case library | Learning Android and iOS testing methods and vulnerability patterns | 移动安全漏洞挖掘专家SKILL，基于 HackerOne 真实报告的移动安全漏洞挖掘知识库，提供 Android 和 iOS 应用的漏洞挖掘手法、技术细节和代码模式分析。 | Yes · 2026-04-19 | None |

## Browser Automation and Traffic Analysis

> Browser control, anti-detection environments, proxy capture, protocol analysis, and all-in-one reverse engineering workstations.

| Project | Type | Core Focus | Best For | GitHub Description | Recently Updated | Latest Release |
| --- | --- | --- | --- | --- | --- | --- |
| [DrissionPage MCP](https://github.com/wxhzhwxhzh/DrissionPageMCP) | MCP | General-purpose browser automation | Page interaction, DOM inspection, authentication, and data collection | 基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用 | No · 2026-02-12 | None |
| [reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer) | Agent / CLI | Generating typed API clients from endpoints used by websites | Browser traffic capture, endpoint discovery, HAR analysis, and Python/JS/TS client generation | The agent that turns websites into APIs! | Yes · 2026-07-05 | [v0.10.0](https://github.com/kalil0321/reverse-api-engineer/releases/tag/v0.10.0) · 2026-06-01 |
| [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp) | MCP | Anti-detection and privacy-focused browser automation | Fingerprint controls, proxies, session isolation, and realistic browser environments | No description | Yes · 2026-07-07 | [v2.3.0](https://github.com/whit3rabbit/camoufox-mcp/releases/tag/v2.3.0) · 2026-07-06 |
| [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp) | MCP | AI integration for Charles Proxy | Live traffic, historical sessions, and request analysis | Charles Proxy MCP server for AI agents with live capture, structured traffic analysis, and agent-friendly tool contracts | Yes · 2026-06-23 | [v3.0.3](https://github.com/heizaheiza/Charles-mcp/releases/tag/v3.0.3) · 2026-04-21 |
| [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) | Desktop Workstation | All-in-one protocol and reverse engineering analysis | Integrated browser, proxy, hooking, AI, and MCP workflows | 全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE &#124; All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration | Yes · 2026-07-13 | [v3.6.52](https://github.com/Mouseww/anything-analyzer/releases/tag/v3.6.52) · 2026-07-13 |
| [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) | Custom Browser / Agent | Engine-level tracing for JS, JSVMP, and WASM | Advanced obfuscation, dynamic code, and low-level execution tracing | 🦊 内置 AI 逆向 Agent 的 Firefox — 通用 JS/JSVMP/WASM/签名逆向工作站，SpiderMonkey 引擎层非侵入 trace，把加密参数从黑盒还原成不依赖浏览器的纯算法 | Yes · 2026-07-13 | [v0.22.2](https://github.com/WhiteNightShadow/firefox-reverse/releases/tag/v0.22.2) · 2026-07-13 |

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
