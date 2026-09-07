# Research project starter

本模板用于建立新研究自己的定义和记录，研究参数保持未定义。将本目录复制到你自己命名的新项目目录；不要覆盖已有项目。填写合同后再创建任务需要的数据/代码/结果子目录，不必一次生成空目录树。

## 第一次使用

1. 阅读本模板的 AGENTS.md，填写 [config/study_contract.yaml](config/study_contract.yaml)。null/空列表表示尚未定义，不是默认选择。记录已批准内容及日期。
2. 在 [docs/variable_dictionary.csv](docs/variable_dictionary.csv) 填字段含义、单位、编码、时间与出处；仅登记字段，不填受试者值。
3. 在 [docs/decision_log.md](docs/decision_log.md) 记录稳定决定与未决项。已有项目先复用现有文档，不强制改名或建立 MEMORY。
4. 每次分析填 [logs/run_manifest.csv](logs/run_manifest.csv)；在模型实际运行后才写 completed。
5. 写作前填写 [docs/claim_ledger.csv](docs/claim_ledger.csv)，检索时填 [docs/literature_search_log.csv](docs/literature_search_log.csv)。

推荐按需结构：data/raw、data/processed、data/derived；code/data_processing、code/analysis、code/figures；results/tables、results/figures、results/reports；intermediate、logs、docs、tests。已有原数据保持原地只读，通过合同记录位置。

新项目开始时可用的提示：

> 阅读项目 AGENTS.md 和已填写的 study_contract.yaml，核对当前数据与字段说明。先完成输入/样本/时间定义检查，指出影响本任务的真实缺口，再执行已授权部分。不要继承任何其他项目的疾病编码、阈值、协变量或分析结论。

本模板没有统计执行器、自动安装器或定时任务。需要少量复用 Skills 时先查个人已安装版本和项目内技能，逐个调用；只安装当前任务需要的一项技能。Playbooks 是阅读资料，可只复制与任务有关的一份并保留自己的项目决策。
