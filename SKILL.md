---
name: dcu-kb
description: 面向海光 HCU/DCU 的本地 DTK/HIP 手册检索与开发知识导航，按任务定位 API、编译、算子、profiling、内存和多卡相关章节。适用于有海光背景的 HIP kernel、DTK/DCC、rocBLAS/hipBLASLt、MIOpen、MIGraphX 和 ONNX Runtime 问题；不将手册结论泛化到其他版本或所有 ROCm 平台。
---

# DCU 开发手册导航

按实际 DTK/库版本查手册中的签名、约束、示例和参数，再结合本机代码验证。此技能只携带原创导航和脚本，不携带手册正文；用户须自行取得有权使用的文档。

## 定位文档

运行只读助手，按优先级解析：
1. `--docs-root`；
2. 环境变量 `DCU_KB_DOCS_ROOT`；
3. 技能目录的 `config.local.json` 中 `docs_root`；
4. 技能目录的 `manuals/`。

```text
python -X utf8 <skill目录>/scripts/find_manuals.py --docs-root <本地手册目录>
python -X utf8 <skill目录>/scripts/find_manuals.py --query hipprof --docs-root <本地手册目录>
```

路径相对配置文件解析；显式指定的目录无效时报告失败，不悄悄换另一个目录。助手只枚举索引中的文件，不读取正文，不搜索整台电脑。缺文档时可以继续查对应版本官方资料，但说明哪些事实尚未由手册确认，不用猜测补齐。

## 按任务选择手册

完整文件名、版本和用途见 [手册索引](references/manual-index.json)。索引基线包含 DTK 26.04、MIGraphX 5.2.0 和 ONNX Runtime 1.19.2，不代表本机一定安装这些版本。

| 任务 | 起始索引 |
|---|---|
| 驱动/DTK 安装与环境变量 | environment、installation |
| HIP kernel、线程和内存模型、多卡编程 | hip-guide，必要时 hip-runtime |
| 查询 hip* API 精确签名与语义 | hip-runtime |
| 编译选项、宏、CUDA 迁移 | dcc，结合 hip-guide / hip-runtime |
| GEMM、矩阵布局、支持类型 | hipblaslt、rocblas；性能方法读 best-practices |
| 卷积等原语 | miopen |
| 性能分析与工具参数 | hipprof，结合 best-practices |
| ONNX 图转换、优化和量化 | migraphx、onnxruntime |

## 阅读和使用证据

- 先列实际文件并确认版本；用关键词搜索章节标题、符号或错误文本，再读取小段上下文。不要一次加载全部手册，章节编号可能随版式变化。
- 只在确有需要时跨读其他手册。确认单个 API 的声明、适用条件、单位、同步语义、示例及返回值；工具参数同时查安装版本的 `--help`。
- 明确区分“手册原文结论”“源码/实机验证”“待验证假设”；引用手册文件、版本、章节/行号，或对应版本官方链接。手册与运行环境不一致时解释差异。
- 编译目标从实际设备确认，不预设所有海光设备都是 gfx906。不要固定 DTK 与 ROCm/CUDA 的一一对应，不跨版本照搬 API、flag、opset 或支持列表。
- 精度、布局、算法、库与后端以支持范围和测量选择，不预设 FP16 总是最佳、某库总是最快、所有大模型都应使用 MIGraphX。
- 多卡区分设备可见性、索引、P2P、collective 与节点拓扑，不将 collective 误限为多机专用。内存回收与异步语义需查实际 API 和运行状态，不编造工具选项。
- 提供最小可用方案，并做与修改相关的编译、正确性或性能验证；读取技能不额外授予安装、启动服务或占用共享设备的权限。

## 与推理生态技能配合

`hygon-inference-optimize` 可用于发现 HYGON-AI 官方仓库、模型部署样例、框架/插件/算子的实际调用路径及端到端 SLA 优化。本技能负责手册级查证；两个技能可独立安装，不能因某个可选技能缺失而停止可完成的手册检索。
