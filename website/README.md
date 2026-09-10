# Website

当前公开入口为仓库 README 与 `tables/` 的 Markdown 表格。本阶段不部署网站。

后续网站应从 `data/libero_results.jsonl` 读取实验，支持按 track、来源、模型、设置、suite 与 checkpoint 状态筛选。
必须显示来源链接和 null，不把不同来源合并为模型唯一分数；WAM 数据为同一事实源的子集，不能重复计数。
