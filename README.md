<div align="center">

# 🔮 Awesome AI Reverse Engineering

**AI 驱动的逆向工程工具、MCP、Skill 与 Agent 集合**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--07-orange.svg)

*当大语言模型进入浏览器、反编译器、调试器和抓包工具，逆向工程的工作方式开始发生变化。*

</div>

---

## 📖 项目简介

Awesome AI Reverse Engineering 是一份围绕 **AI + 逆向工程** 生态整理的工具清单，收录 MCP 服务器、Claude Code/Cursor/Codex 可用的 Skill、IDA Pro/Ghidra/Binary Ninja/JADX 插件、浏览器自动化与流量分析工具、Android/iOS 动态分析工具，以及 AI 驱动的完整逆向 Agent 与桌面工作站。

这些工具让大语言模型不再只是“解释一段代码”，而是直接参与真实分析：操作浏览器、设置断点与注入 Hook、分析 JS/WASM/混淆代码、驱动反编译器、控制设备与插桩、读取流量，并生成分析报告与调用链。

---

## 🧩 工具形态说明

| 形态              | 作用                                          |
| --------------- | ------------------------------------------- |
| **MCP Server**  | 把浏览器、反编译器、调试器或设备能力提供给 AI 调用                 |
| **Skill**       | 为 AI 提供分析方法、任务步骤、判断标准和输出规范                  |
| **IDE / RE 插件** | 把 AI 能力集成到 IDA、Ghidra、JADX、Binary Ninja 等工具 |
| **Agent**       | 根据目标自主规划、调用工具、验证结果并生成报告                     |
| **桌面工作站**       | 将抓包、浏览器、Hook、AI 分析和结果管理集成在一个应用中             |
| **知识库**         | 为 AI 提供漏洞模式、案例和测试思路，但不直接执行分析操作              |

> **MCP 提供操作能力，Skill 提供分析方法，AI Agent 负责规划、验证和总结。**

---

## 📑 目录

* [快速选型](#-快速选型)
* [JavaScript 与 Web 逆向](#-javascript-与-web-逆向)
* [二进制与原生程序逆向](#-二进制与原生程序逆向)
* [Android 与 iOS 安全分析](#-android-与-ios-安全分析)
* [浏览器自动化与流量分析](#-浏览器自动化与流量分析)
* [工具评估维度](#-工具评估维度)
* [使用规范](#-使用规范)
* [贡献指南](#-贡献指南)

---

# 🚀 快速选型

| 需求                              | 推荐项目                              |
| ------------------------------- | --------------------------------- |
| 普通网页签名、参数和 Cookie 定位            | JS Reverse MCP                    |
| 综合型 JS、WASM、AST 和网络分析           | jshookmcp                         |
| Worker、Webpack、JSVMP 等高级 Web 逆向 | reverse-skill                     |
| 将浏览器加密函数封装成接口                   | js-reverse-automation--skill      |
| 强调证据沉淀和本地复现                     | JSReverser-MCP                    |
| 反检测浏览器环境                        | Camoufox MCP Server               |
| 微信小程序运行时分析                      | MiniApp CDP MCP                   |
| IDA Pro 实时 AI 分析                | IDA Pro MCP                       |
| IDA 文件导出后交给 AI 分析               | IDA-NO-MCP                        |
| 无头 IDA 服务                       | ida-mcp-rs                        |
| Ghidra AI 集成                    | GhidraMCP                         |
| Binary Ninja AI 集成              | Binary Ninja MCP                  |
| 多工具二进制自动化平台                     | revula                            |
| Android API 提取和调用链分析            | Android Reverse Engineering Skill |
| JADX 内交互式 AI 分析                 | JADX-AI-MCP                       |
| Android 动态 Hook                 | Frida MCP Server                  |
| Android 设备自动化                   | ADB MCP Server                    |
| Android 抓包与流量查询                 | Android Proxy MCP                 |
| Charles 流量接入 AI                 | Charles MCP Server                |
| 一体化协议分析工作站                      | Anything Analyzer                 |
| 引擎级 JS、JSVMP、WASM 追踪            | Firefox-Reverse                   |

---

# 🌐 JavaScript 与 Web 逆向

> JavaScript 运行时调试、请求链定位、Hook、混淆还原、WASM、协议分析和本地算法复现。

## 综合型 MCP

| 项目                                                                 | 形态        | 核心定位                | 适用场景                                           |
| ------------------------------------------------------------------ | --------- | ------------------- | ---------------------------------------------- |
| [jshookmcp](https://github.com/vmoranv/jshookmcp)                  | MCP       | 综合型 AI JS 安全分析平台    | 浏览器自动化、CDP、网络监控、JS Hook、WASM、Source Map、AST 变换 |
| [JS Reverse MCP](https://github.com/zhizhuodemao/js-reverse-mcp)   | MCP       | 面向真实浏览器运行时的 JS 调试工具 | 请求参数、动态 Cookie、WebSocket、调用链和关键函数定位            |
| [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP)      | MCP / 工作流 | 标准化 Web 逆向流程        | 页面观察、运行时采样、本地复现、补环境和证据沉淀                       |
| [MiniApp CDP MCP](https://github.com/zhizhuodemao/miniapp-cdp-mcp) | MCP       | 微信小程序 CDP 调试工具      | 微信开发者工具、PC 微信小程序、运行时代码和请求分析                    |

---

## jshookmcp

**定位：能力覆盖较广的综合型 JavaScript 逆向 MCP。**

jshookmcp 尝试把多个逆向环节整合到统一接口中，包括：

* 浏览器自动化；
* Chrome DevTools Protocol 调试；
* 网络请求和响应监控；
* JavaScript Hook；
* AST 代码变换；
* Source Map 重建；
* WebAssembly 分析；
* 页面脚本和运行时数据采集。

它更接近面向 AI Agent 的“JS 逆向能力平台”，适合需要浏览器、网络、代码和运行时数据协同分析的场景。

**适合：**

* 复杂网页签名分析；
* 大规模脚本检索；
* WASM 与 JavaScript 混合逻辑；
* 多种分析工具联动；
* 构建团队级逆向 Agent。

对于仅需读取几个请求或设置简单断点的任务，综合型工具可能存在一定的配置和使用成本。

---

## JS Reverse MCP

**定位：以真实浏览器调试为核心的 JavaScript 逆向 MCP。**

该项目主要让 Claude Code、Cursor、Codex 等 AI 客户端进入真实浏览器运行环境，直接观察：

* 页面加载过程；
* 请求和响应内容；
* WebSocket 消息；
* JavaScript 源码；
* 断点和调用栈；
* 变量、函数参数和返回值；
* 登录态和页面运行状态。

**适合：**

* 登录参数和签名参数定位；
* 动态 Cookie 分析；
* 请求发起位置查找；
* WebSocket 协议分析；
* 复杂前端调用链追踪。

它适合作为通用 Web 逆向环境的基础 MCP，再搭配流程型 Skill 使用。

---

## JSReverser-MCP

**定位：强调证据、复现和任务产物的标准化逆向工作流。**

该项目不只关注“找到某个变量”，而是希望将完整过程沉淀下来：

1. 观察页面行为；
2. 捕获关键请求；
3. 采集运行时数据；
4. 定位相关源码；
5. 建立调用链；
6. 提取必要环境；
7. 在本地重建逻辑；
8. 保存样本、证据和分析结论。

它更适合团队协作、长期维护和需要稳定复现的任务。

---

## MiniApp CDP MCP

**定位：微信小程序运行时调试专用 MCP。**

普通 Chrome 调试工具通常无法直接覆盖微信小程序运行环境。MiniApp CDP MCP 通过 Chrome DevTools Protocol 连接：

* 微信开发者工具；
* PC 端微信小程序；
* 小程序 JavaScript 运行时。

**适合：**

* 小程序接口和请求参数分析；
* 打包代码搜索；
* 鉴权和签名函数定位；
* 运行时变量读取；
* 小程序调用链分析。

---

## JS 逆向 Skill

| 项目                                                                                         | 形态         | 核心定位                | 适用场景                                |
| ------------------------------------------------------------------------------------------ | ---------- | ------------------- | ----------------------------------- |
| [hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill)       | Skill      | 基于反检测浏览器的完整 JS 逆向流程 | 网络捕获、源码定位、Hook、算法还原和本地复现            |
| [js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) | Skill      | JS 逆向成果服务化          | JSRPC、Flask、autoDecoder、请求加密和响应解密   |
| [JSHook Reverse Tool](https://github.com/wuji66dde/jshook-skill)                           | Skill / 工具 | 代码采集、反混淆和 Hook 辅助   | 大型脚本采集、加密检测、CDP 和增量分析               |
| [reverse-skill](https://github.com/715494637/reverse-skill/)                               | Skill      | 高级 Web 逆向方法库        | JSVMP、Worker、WASM、Webpack、AST 和协议分析 |
| [xbsReverseSkill](https://github.com/lwjjike/xbsReverseSkill)                              | Skill 套件   | 模块化 Web 逆向能力        | AST、纯算法、协议分析、浏览器补环境                 |

---

## hello_js_reverse_skill

**定位：围绕反检测浏览器建立的完整 JS 逆向方法论。**

该 Skill 重点描述一条完整的分析路径：

> 网络捕获 → 源码定位 → 运行时 Hook → 数据流验证 → 算法还原 → 本地复现。

它的价值主要体现在分析方法和过程约束，而不是单独提供浏览器调试引擎。

**适合：**

* 已经安装浏览器 MCP，但缺乏系统分析流程；
* 希望将浏览器逻辑还原为 Python 或 Node.js；
* 需要输出完整分析证据；
* 目标页面存在自动化检测。

---

## js-reverse-automation--skill

**定位：将逆向得到的浏览器函数转化为稳定服务。**

该项目围绕以下组件组织自动化方案：

* chrome-devtools-mcp；
* JSRPC；
* Flask；
* autoDecoder；
* 浏览器内函数调用；
* 请求加密和响应解密。

它更关注逆向结果的工程化使用。

**适合：**

* 将网页加密函数暴露为 HTTP API；
* 建立登录参数加密服务；
* 自动执行响应解密；
* 与 Burp 或爬虫程序联动；
* 将一次性分析结果变成可复用服务。

---

## JSHook Reverse Tool

**定位：包含代码采集、Hook 和 AI 分析流程的 JavaScript 逆向 Skill。**

主要能力包括：

* 页面脚本采集；
* 混淆代码处理；
* 加密算法特征检测；
* CDP 调试；
* Hook 注入；
* 大型脚本摘要；
* 增量采集和优先级分析。

适合用于大型前端工程和代码量较大的页面。

---

## reverse-skill

**定位：覆盖高级 Web 逆向问题的流程型 Skill。**

该项目覆盖：

* 请求链定位；
* 运行时诊断；
* AST 混淆恢复；
* JSVMP；
* Web Worker；
* WebAssembly；
* Webpack Runtime；
* 协议语义分析。

**适合：**

* 核心逻辑运行在 Worker 中；
* 代码经过虚拟机混淆；
* 参数由多个 Webpack 模块动态组合；
* 普通断点难以定位；
* JavaScript 与 WASM 深度混合。

它可以视为浏览器 MCP 的高级分析手册。

---

## xbsReverseSkill

**定位：按问题类型拆分的模块化 Web 逆向 Skill。**

主要方向包括：

* AST 反混淆；
* 纯算法逆向；
* 协议分析；
* 浏览器补环境；
* 验证逻辑分析。

模块化结构适合按任务加载：

* 代码难以阅读：使用 AST 模块；
* 已定位核心函数：使用纯算法模块；
* Node.js 无法执行：使用补环境模块；
* 请求流程复杂：使用协议分析模块。

---

## 专用 Web 安全分析工具

| 项目                                                    | 形态  | 核心定位          | 适用场景                    |
| ----------------------------------------------------- | --- | ------------- | ----------------------- |
| [ruishu-mcp](https://github.com/xuange520/ruishu-mcp) | MCP | 动态 WAF 流量研究工具 | 授权环境中的瑞数类动态防护、请求参数和流量分析 |

### ruishu-mcp

**定位：面向特定动态 WAF 场景的专用 MCP。**

它不是通用浏览器自动化框架，而是用于研究动态脚本、防护页面和真实业务流量之间的关系。

适合在自有系统或明确授权环境中进行：

* 动态防护行为研究；
* 请求参数和 Cookie 分析；
* 防护流量与业务流量分离；
* AI 辅助协议理解。

---

# 🔬 二进制与原生程序逆向

> IDA Pro、Ghidra、Binary Ninja、调试器、反汇编器以及自动化二进制分析。

| 项目                                                                | 形态              | 核心定位                             | 适用场景                 |
| ----------------------------------------------------------------- | --------------- | -------------------------------- | -------------------- |
| [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)               | IDA 插件 / 导出工具   | 将 IDA 数据导出后交给 AI IDE 分析          | 大规模代码索引、低交互成本分析      |
| [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp)            | MCP             | AI 直接读取和操作 IDA Pro               | 反编译、交叉引用、重命名、注释和类型恢复 |
| [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)              | MCP             | Rust 实现的无头 IDA 服务                | 服务端部署、自动化流水线         |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP)             | Ghidra 插件 / MCP | Ghidra 与 AI 客户端连接                | 反编译、函数分析和符号整理        |
| [Binary Ninja MCP](https://github.com/fosdickio/binary_ninja_mcp) | 插件 / MCP        | Binary Ninja AI 桥接               | 多目标二进制实时分析           |
| [revula](https://github.com/president-xd/revula)                  | MCP 平台          | 通用逆向工程自动化后端                      | 静态分析、动态调试、恶意软件和批量处理  |
| [Rikugan](https://github.com/buzzer-re/Rikugan)                   | Agent / 插件      | 嵌入 IDA 和 Binary Ninja 的 AI Agent | 在逆向界面中进行连续对话式分析      |
| [reverse-skill](https://github.com/zhaoxuya520/reverse-skill)     | Skill / Router  | 安全任务和工具链路由                       | 多工具编排、CTF、安全研究和报告生成  |

---

## IDA-NO-MCP

**定位：不依赖 MCP 交互的 IDA AI 分析方案。**

它将 IDA 中的内容导出为普通文件，例如：

* 反编译代码；
* 反汇编代码；
* 字符串；
* 导入表和导出表；
* 函数调用关系；
* 内存数据。

随后由 Cursor、Claude Code、Codex 等 AI 编程工具使用文件搜索、代码索引和 Shell 能力进行分析。

**优势：**

* 配置相对简单；
* AI 可以进行全局代码检索；
* 适合大型程序；
* 减少频繁 MCP 调用。

**限制：**

它偏向单向导出，AI 通常无法像实时 MCP 一样直接修改 IDA 数据库。

---

## IDA Pro MCP

**定位：IDA Pro 与 AI 客户端之间的实时交互接口。**

可用于让 AI：

* 读取反编译代码；
* 获取汇编代码；
* 查询交叉引用；
* 查找字符串和函数；
* 修改函数名称；
* 添加注释；
* 辅助恢复变量和类型；
* 分析调用链。

适合以 IDA Pro 为主要分析环境，并希望 AI 直接参与 IDB 整理的用户。

---

## ida-mcp-rs

**定位：Rust 实现的无头 IDA MCP。**

更偏向：

* 服务器部署；
* 自动化分析；
* 命令行环境；
* 批量文件处理；
* CI 或内部分析平台。

与桌面型 IDA MCP 相比，它更强调无头运行和工程部署。

---

## GhidraMCP

**定位：Ghidra 用户的 AI 接入工具。**

主要用于：

* 获取反编译结果；
* 查询函数和类；
* 查看导入导出；
* 修改函数和变量名称；
* 辅助整理程序结构。

适合恶意软件、固件、普通二进制和跨平台程序分析。

---

## Binary Ninja MCP

**定位：Binary Ninja 插件与 MCP 桥接工具。**

它让 AI 客户端可以读取 Binary Ninja 的分析结果，并在多个二进制目标之间切换。

适合已经将 Binary Ninja 作为主要逆向环境的研究人员。

---

## revula

**定位：整合多种底层逆向工具的通用自动化平台。**

其设计方向包括整合：

* LIEF；
* Capstone；
* radare2；
* objdump；
* FLOSS；
* YARA；
* Capa；
* Ghidra；
* GDB；
* LLDB；
* Frida。

可覆盖：

* 文件结构解析；
* 反汇编；
* 字符串提取；
* 熵分析；
* YARA 和能力规则扫描；
* 反编译；
* 动态断点；
* 内存检查；
* 代码覆盖率分析。

适合构建恶意软件分析、CTF、批量逆向和多架构分析平台。

---

## Rikugan

**定位：直接运行在 IDA Pro 和 Binary Ninja 界面中的 AI 逆向 Agent。**

与外部 MCP 不同，它强调在逆向软件内部提供连续的 AI 交互。

可以辅助：

* 导航函数；
* 查看反编译和汇编代码；
* 查询交叉引用；
* 分析类型；
* 添加注释；
* 执行脚本；
* 处理部分中间表示或微码。

适合不希望频繁切换 AI IDE 和逆向软件的用户。

---

## reverse-skill

**定位：安全任务路由和工具链编排 Skill。**

该项目不依赖单一逆向软件，而是根据任务类型选择不同工具和流程。

适合：

* 逆向工程；
* CTF；
* 授权安全测试；
* Burp 和 Kali 环境；
* 多 Skill 编排；
* 经验记录和报告生成。

它更像多工具环境的总入口，而不是具体的反编译器。

---

# 📱 Android 与 iOS 安全分析

> APK 反编译、API 提取、动态插桩、设备管理、流量分析和移动安全知识库。

| 项目                                                                                                       | 形态            | 核心定位                 | 适用场景                                    |
| -------------------------------------------------------------------------------------------------------- | ------------- | -------------------- | --------------------------------------- |
| [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Skill         | Android 静态分析与 API 提取 | APK、XAPK、JAR、AAR、Retrofit、OkHttp 和调用链分析 |
| [JADX-AI-MCP](https://github.com/zinja-coder/jadx-ai-mcp)                                                | JADX 插件 / MCP | JADX 内实时 AI 分析       | APK 代码阅读、漏洞分析和上下文审查                     |
| [Frida MCP Server](https://github.com/zhizhuodemao/frida-mcp)                                            | MCP           | Android 动态插桩         | Java、Native Hook、参数和返回值采集               |
| [Android Proxy MCP](https://github.com/zhizhuodemao/android_proxy_mcp)                                   | MCP           | Android 流量采集和查询      | HTTP、HTTPS 请求筛选、搜索和内容分析                 |
| [ADB MCP Server](https://github.com/zhizhuodemao/adb-mcp)                                                | MCP           | Android 设备自动化        | 安装、启动、截图、录屏、文件和 Logcat                  |
| [iOS MCP](https://github.com/witchan/ios-mcp)                                                            | MCP           | 越狱 iOS 设备控制          | 应用、文件、日志、HID 和辅助功能操作                    |
| [android-h1](https://github.com/s7safe/android-h1)                                                       | Skill / 知识库   | 移动安全漏洞案例库            | Android、iOS 测试方法和漏洞模式学习                 |

---

## Android Reverse Engineering Skill

**定位：Android 静态分析和 HTTP API 提取 Skill。**

支持分析：

* APK；
* XAPK；
* JAR；
* AAR；
* Kotlin 和 Java 代码；
* Retrofit；
* OkHttp；
* Volley；
* Ktor；
* GraphQL；
* 硬编码 URL；
* HMAC 和鉴权逻辑。

它重点解决：

* App 调用了哪些接口；
* 参数从哪里生成；
* 请求经过哪些 Repository、ViewModel 或 UseCase；
* 是否存在硬编码密钥或地址；
* 请求签名和鉴权逻辑位于哪里。

适合将 APK 转换为接口文档、调用链和初步安全分析报告。

---

## JADX-AI-MCP

**定位：将 AI 实时接入 JADX 的 Android 逆向插件。**

AI 可以围绕当前代码上下文进行：

* 类和方法解释；
* 调用关系分析；
* 数据流追踪；
* 漏洞模式检查；
* 混淆代码辅助理解；
* 关键业务逻辑定位。

与批处理型 Skill 相比，它更适合在 JADX 图形界面中持续阅读和深入分析。

---

## Frida MCP Server

**定位：将 Frida 动态分析能力提供给 AI。**

适合：

* Spawn 或 Attach 应用；
* Hook Java 方法；
* Hook Native 函数；
* 记录参数和返回值；
* 采集调用栈；
* 验证静态分析结论；
* 观察运行时加密和解密数据。

它属于动态分析接入层，通常需要与 JADX、ADB 和流量分析工具配合。

---

## Android Proxy MCP

**定位：让 AI 查询和分析 Android HTTP/HTTPS 流量。**

主要工作方式是：

1. 通过代理工具采集流量；
2. 将请求和响应保存到数据库；
3. 通过 MCP 进行筛选、搜索和读取；
4. 让 AI 对流量进行摘要和分析。

适合：

* 按域名筛选请求；
* 查找特定参数；
* 搜索请求体和响应体；
* 分析 JSON 或长文本响应；
* 与 Frida 联动观察加密前后的数据。

---

## ADB MCP Server

**定位：Android 设备控制基础设施。**

主要提供：

* 设备信息；
* APK 安装和卸载；
* 应用启动和停止；
* 点击、滑动和文本输入；
* 截图和录屏；
* 文件上传和下载；
* Logcat 日志读取；
* 多设备管理。

它本身不负责反编译或算法分析，而是为 Android AI Agent 提供设备操作能力。

---

## iOS MCP

**定位：运行在越狱 iPhone 上的 iOS 设备控制 MCP。**

可涉及：

* 应用管理；
* 文件系统；
* 剪贴板；
* 系统和应用日志；
* HID 输入；
* 辅助功能节点；
* UI 操作。

适合越狱设备上的安全研究、自动化测试和 Agent 控制。

---

## android-h1

**定位：基于移动安全案例整理的测试知识库。**

覆盖方向包括：

* Android 组件安全；
* iOS URL Scheme；
* Deep Link；
* WebView；
* 业务逻辑漏洞；
* 双因素认证绕过；
* 本地数据保护；
* 移动端常见漏洞模式。

该项目主要用于：

* 生成测试清单；
* 学习漏洞案例；
* 为 AI 提供测试思路；
* 辅助建立安全假设。

它不是自动化扫描器，知识库内容应结合真实代码和运行结果进行验证。

---

# 🌍 浏览器自动化与流量分析

> 浏览器控制、反检测环境、代理抓包、协议分析和一体化逆向工作站。

| 项目                                                                     | 形态            | 核心定位                   | 适用场景                    |
| ---------------------------------------------------------------------- | ------------- | ---------------------- | ----------------------- |
| [DrissionPage MCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)      | MCP           | 通用浏览器自动化               | 页面操作、DOM 读取、登录和数据采集     |
| [Camoufox MCP Server](https://github.com/whit3rabbit/camoufox-mcp)     | MCP           | 反检测和隐私浏览器自动化           | 指纹控制、代理、多会话隔离和真实浏览器环境   |
| [Charles MCP Server](https://github.com/heizaheiza/Charles-mcp)        | MCP           | Charles Proxy AI 接入    | 实时流量、历史 Session 和请求分析   |
| [Anything Analyzer](https://github.com/Mouseww/anything-analyzer)      | 桌面工作站         | 一体化协议和逆向分析             | 浏览器、代理、Hook、AI 和 MCP 集成 |
| [Firefox-Reverse](https://github.com/WhiteNightShadow/firefox-reverse) | 定制浏览器 / Agent | 引擎级 JS、JSVMP 和 WASM 追踪 | 高级混淆、动态代码和底层执行轨迹分析      |

---

## DrissionPage MCP

**定位：基于 DrissionPage 的通用浏览器自动化 MCP。**

主要用于：

* 打开网页；
* 定位元素；
* 点击和输入；
* 获取 DOM；
* 执行 JavaScript；
* 完成登录流程；
* 采集网页内容。

适合普通浏览器操作和数据采集。涉及复杂断点、源码映射和调用栈时，建议配合专业 JS 逆向 MCP。

---

## Camoufox MCP Server

**定位：强调隐私、隔离和反检测能力的浏览器 MCP。**

可能涉及：

* 浏览器指纹控制；
* 操作系统特征模拟；
* WebRTC 和 WebGL 控制；
* 代理配置；
* 会话隔离；
* 光标行为模拟；
* 图片和资源加载控制。

适合：

* 需要接近真实用户环境的浏览器任务；
* 多会话自动化；
* 代理和隐私场景；
* 为 JS 逆向 Skill 提供运行环境。

---

## Charles MCP Server

**定位：将现有 Charles Proxy 工作流接入 AI。**

适合已经使用 Charles 的开发者和研究人员。

AI 可以辅助：

* 读取实时流量；
* 分析历史 Session；
* 按域名或接口筛选；
* 对请求和响应进行摘要；
* 查找异常参数；
* 分析移动端和桌面端协议。

它的重点是连接现有 Charles 环境，而不是重新实现抓包代理。

---

## Anything Analyzer

**定位：桌面化、一体化的协议分析工作站。**

尝试将以下能力整合到一个应用中：

* 浏览器操作；
* MITM 流量代理；
* JavaScript Hook；
* 浏览器指纹控制；
* AI 分析；
* MCP Server；
* 请求和响应可视化；
* 分析结果管理。

适合：

* 希望减少工具安装和组合成本；
* 以协议和流量分析为主要目标；
* 同时处理网页、桌面应用、命令行程序和移动端流量；
* 希望使用可视化界面完成分析。

---

## Firefox-Reverse

**定位：从 Firefox 和 SpiderMonkey 引擎层追踪代码执行的逆向工作站。**

适合普通 CDP 和 Hook 难以稳定分析的场景：

* JavaScript 动态生成；
* 函数频繁替换；
* JSVMP；
* WebAssembly；
* 复杂反调试；
* Hook 容易被检测；
* 需要恢复底层数据流和执行轨迹。

它的目标通常不是只获取某一次签名结果，而是帮助还原能够脱离浏览器运行的算法逻辑。

---

# 📊 工具评估维度

在选择项目时，建议从以下维度进行判断。

## 1. 工具形态

* MCP；
* Skill；
* 插件；
* Agent；
* 桌面应用；
* 知识库。

Skill 通常不能替代真实操作工具，MCP 也不能替代系统化分析方法。

---

## 2. 分析方式

* 静态分析；
* 动态分析；
* 流量分析；
* 设备控制；
* 浏览器自动化；
* 代码重建；
* 报告生成。

---

## 3. 是否支持写操作

部分项目只能读取分析结果，另一些项目可以：

* 重命名函数；
* 修改变量；
* 添加注释；
* 设置断点；
* 执行 Hook；
* 操作设备；
* 修改浏览器状态。

涉及写操作时，应注意备份分析数据库和测试环境。

---

## 4. 上下文占用

MCP 工具数量过多时，工具定义可能占用大量模型上下文。

建议关注：

* 工具是否支持按需加载；
* 是否支持搜索式工具发现；
* 是否提供摘要；
* 是否能够分片读取数据；
* 是否能只返回当前任务需要的内容。

---

## 5. 任务产物

成熟的逆向工作流不应只输出自然语言结论，还应保存：

* 请求和响应样本；
* Hook 脚本；
* 函数调用链；
* 关键代码；
* 环境依赖；
* 本地复现代码；
* 失败尝试；
* 分析证据；
* 最终报告。

---

## 6. 部署方式

* 本地桌面；
* 无头服务；
* Docker；
* 虚拟机；
* 越狱设备；
* Root Android 设备；
* 浏览器扩展；
* IDE 插件。

部署方式会直接影响使用成本和适用范围。

---

## 7. 项目维护情况

使用前建议检查：

* 最近提交时间；
* Issue 响应情况；
* Release 版本；
* 安装文档；
* 支持的客户端；
* 支持的软件版本；
* License；
* 是否存在未完成或实验性功能。

本列表收录不代表对项目安全性、稳定性或持续维护状态作出保证。

---

# ⚠️ 使用规范

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

---

# 🤝 贡献指南

欢迎提交新的 AI 逆向工程项目。

建议提交的项目至少满足以下条件之一：

* 提供逆向相关 MCP Server；
* 提供可复用的逆向 Skill；
* 将 AI 集成到逆向软件；
* 提供 AI 驱动的静态或动态分析能力；
* 提供浏览器、设备或抓包工具的 AI 接口；
* 提供完整的逆向 Agent 或工作站。

提交项目时建议包含：

```markdown
| [项目名称](项目地址) | 项目形态 | 一句话核心定位 | 主要适用场景 |
```

同时建议说明：

* 支持的平台；
* 安装方式；
* 支持的 AI 客户端；
* 是否需要商业软件；
* 是否需要 Root 或越狱环境；
* License；
* 最近维护时间。

不建议收录：

* 没有源码或文档的项目；
* 仅有概念介绍、没有可运行实现的项目；
* 长期失效且没有替代价值的项目；
* 主要用于未授权攻击、账号窃取或恶意绕过的工具；
* 与 AI 或逆向工程关系较弱的普通自动化项目。

---

# 🗺️ 生态总结

AI 逆向工程正在逐渐形成一套新的分层体系：

```text
大语言模型 / AI Agent
          │
          ▼
   Skill 与任务工作流
          │
          ▼
      MCP 接口层
          │
          ▼
浏览器 / IDA / Ghidra / JADX
Frida / ADB / Charles / 调试器
          │
          ▼
  真实代码、流量和运行时数据
```

不同组件承担不同职责：

* **浏览器和逆向软件负责提供事实；**
* **MCP 负责连接 AI 与工具；**
* **Skill 负责约束分析过程；**
* **Agent 负责规划、调用、验证和总结；**
* **本地复现代码负责验证最终结论。**

现阶段通常不存在一个工具可以覆盖所有逆向场景。

更现实的方案是：

> 选择一个主要分析环境，再搭配一至两个专用 MCP 和相应 Skill，构建适合自身任务的工作流。

---

## ⭐ Star History

如果这份列表对你有帮助，欢迎 Star、Fork 或提交 Pull Request。

也欢迎推荐新的 AI 逆向工程工具、MCP、Skill、插件和 Agent。

---

## 📄 License

本列表采用 [MIT License](LICENSE)。

项目列表中的各个工具拥有各自的许可证，使用前请查看对应仓库的 License 和使用说明。
