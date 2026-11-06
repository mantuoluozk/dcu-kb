# dcu-kb

海光 HCU/DCU 本地手册检索技能，覆盖 DTK/HIP、DCC、BLAS、MIOpen、hipprof、MIGraphX 与 ONNX Runtime。将开发任务路由到相关章节，按实际版本查证接口和参数。

## 安装

将本仓库完整复制到你的技能目录，例如 Codex 的 `~/.codex/skills/dcu-kb/`。保留 `SKILL.md`、`agents/`、`references/` 和 `scripts/`。

## 配置文档

本仓库不附带手册正文。自行取得有权使用的 Markdown 手册后，用以下任意方式指定目录：

- 环境变量 `DCU_KB_DOCS_ROOT`；
- 技能目录中新建 `config.local.json`：`{"docs_root": "/path/to/manuals"}`；
- 将文件放在技能目录下的 `manuals/`（已被 Git 忽略）。

命令行 `--docs-root` 优先于这些配置。相对 JSON 路径以配置文件所在目录为基准。手册文件名见 [索引](references/manual-index.json)，允许 HIP 最佳实践文件名有无空格两种写法。

```text
python -X utf8 scripts/find_manuals.py --docs-root <手册目录>
python -X utf8 scripts/find_manuals.py --docs-root <手册目录> --query hipprof
```

退出码：0＝选中手册全部找到；1＝部分缺失或查询无匹配；2＝目录/配置/索引错误。脚本只报告路径，不读取正文。

## 使用

例如：“使用 $dcu-kb，按我安装的 DTK 版本查 HIP 异步拷贝的语义。”

当前索引基于 DTK 26.04 等 12 本手册，不构成未来版本的兼容承诺。技能本身的原创文本与脚本采用 MIT；手册和引用软件的权利、许可独立，本仓库的许可不覆盖它们。

与 [hygon-inference-optimize](https://github.com/mantuoluozk/hygon-inference-optimize) 配合，可进一步查官方开源实现、部署样例与端到端性能优化。
