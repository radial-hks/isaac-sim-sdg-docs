# Project Context

## 基本信息
- **项目名称**: isaac-sim-sdg-docs
- **创建者**: Hermes (千问-max)
- **创建时间**: 2026-06-22 08:00
- **最后更新**: 2026-06-22 10:30
- **状态**: 🟢 稳定可用

## 任务目标
收集 Isaac Sim 6.0 的 SDG 相关文档，建立可迭代更新的离线知识库，支持后续 SDG 工作流开发。

## 关键决策记录（Hermes 每次决策时追加）
| 时间 | 决策 | 理由 |
|------|------|------|
| 2026-06-22 08:00 | 采用增量更新设计而非全量重抓 | 节省时间和带宽，checksum+HEAD 双重检查 |
| 2026-06-22 09:00 | 发现 mojibake 问题并全量重抓 | 质量优先于速度 |
| 2026-06-22 09:30 | url_to_slug 取最后 3 段 | 避免 filename 冲突，262 页零冲突验证通过 |

## 当前进度
- [x] 阶段 1: 项目骨架创建（manifests + 目录结构）✅
- [x] 阶段 2: 16 个模块全量采集（262 页）✅
- [x] 阶段 3: 质量修复（mojibake + slug 冲突）✅
- [x] 阶段 4: 推送到 GitHub ✅
- [ ] 阶段 5: 外部模型代码审查（待执行）⏳

## Hermes 做过的关键操作（Git hook 自动追加）
<!-- 格式：
### YYYY-MM-DD HH:MM - Branch: xxx
Commit: ...
- Files: ...
- Changes summary: ...
-->

### 2026-06-22 08:00 - Branch: master
Commit: init
- Files: manifests/, collect.py, scripts/
- Changes summary: 项目初始化，16 个模块 manifest 定义

### 2026-06-22 09:00 - Branch: master
Commit: collect: 全量抓取 262 页
- Files: source/raw/ (262 files)
- Changes summary: 16 模块全部采集完成

### 2026-06-22 09:30 - Branch: master
Commit: fix: url_to_slug 冲突修复
- Files: collect.py::url_to_slug, tests/test_url_to_slug.py
- Changes summary: 改为取 URL 最后 3 段，262 页零冲突验证通过

### 2026-06-22 10:00 - Branch: master
Commit: docs: README 修复
- Files: README.md
- Changes summary: 修复 stray fence、更新覆盖率 58%→60%（232/385）、output 5MB→3.7MB

### 2026-06-22 10:30 - Branch: master
Commit: push: 初始化推送到 GitHub
- Files: all
- Changes summary: 首次推送到 radial-hks/isaac-sim-sdg-docs

## 待审查项（审查完成后移至"已审查"）
- [ ] 验证 16 个模块的提取质量是否完整
- [ ] 检查 collect.py 的并发逻辑是否有竞态条件
- [ ] 审查 manifest JSON schema 是否需要版本化
- [ ] 评估 output 组装是否需要分章节索引

## 已审查项
- [x] url_to_slug 冲突修复验证（262/262 零冲突）✅
- [x] mojibake 检查（0 occurrences）✅
- [x] 4/4 测试通过 ✅

### 2026-06-21 22:47 - Branch: master
Commit: Unknown
Files changed: 1
- .github/project_context.md

> **Note**: This project uses project-context-injection skill for cross-Agent state sharing.

