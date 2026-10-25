# Python → AI 应用开发 · 学习工作区

本目录是你 28 周计划的实际落地处。所有代码、笔记、诊断、复盘都放这里，用 git 管起来。

> **第一次来，先打开 `START_HERE.md`** —— 那是按顺序排好的 14 件事，照着一件一件做。
> 本文件是参考资料（环境说明、命令速查），不用逐行读。

---

## 一、两份材料的关系（先看这段，别搞反）

| 材料 | 定位 | 用的时间段 |
|---|---|---|
| 《零基础起步手册（前 4 周）》 | **逐日教案**：第 0 周 7 天 + 第 1–3 周，每天学什么、做什么、怎么算过关 | 第 0–4 周 |
| 《AI 应用开发 28 周计划》 | **总纲**：阶段划分、每周主题、验收标准、时间不够时砍什么 | 第 5 周起 |

手册自己写了一句：「现在还需要看那 28 周的计划吗？**先放着。**等你完成这 4 周，再打开它，那时候你能看懂里面 80% 的词。」

**所以顺序是：打完手册的 4 周 → 做 10 题诊断 → 从 28 周计划的第 5 周（HTTP 与 API）接上。**

---

## 二、环境体检（2026-10-25 实测）

| 项目 | 状态 | 位置 / 说明 |
|---|---|---|
| Python | ✅ **3.11.9** | `D:\python\python.exe`，已在 PATH，满足计划要求 3.11+ |
| Git | ✅ **2.56.0** | `C:\Program Files\Git\cmd`，已写入系统 PATH（**新开的终端才生效**） |
| VS Code | ✅ **1.142.0** | `%LOCALAPPDATA%\Programs\Microsoft VS Code`，已在用户 PATH |
| Docker Desktop | ⏸ 延后 | 计划第 10 周部署才用，届时再装（需 WSL2 + 重启） |
| 中文编码 | ✅ 已开 UTF-8 模式 | 用户环境变量 `PYTHONUTF8=1`，避免终端中文乱码 |
| 磁盘 | ✅ C 盘 29 GB 可用 | 已关休眠（释放 12.47 GB）；pip 缓存指向 `E:\pip-cache`。VS Code 数据目录保持默认（junction 方案不可用，见下） |

> **踩坑记录**：曾用目录联接把 `.vscode` 和 `AppData\Roaming\Code` 指向 E 盘，VS Code 启动即报
> `EPERM: operation not permitted, mkdir '...\.vscode\extensions'`。**VS Code 不认 reparse point 做数据目录**，已回退为默认。
> C 盘现在 29GB，没必要为这点空间折腾。

> **VS Code 首次打开后装两个扩展**：`Python`（微软官方）、`Pylance`。计划要求的就这两个，别多装。

---

## 三、第 0 周：3 天完成

> 你之前在学 Java 基础，`if / for / 变量 / 函数` 的概念能直接迁移，所以手册第 0 周可以压缩。

### Day A · 跑通第一行（约 1 小时）

1. 打开 VS Code → 文件 → 打开文件夹 → 选 `E:\project1\python-learn`
2. 装扩展：`Python`、`Pylance`
3. 打开 `week0\day01_hello.py`，按 `Ctrl+F5` 运行
4. 看到「你好」和 2 / 11 / 你好世界 三行输出 → **环境通了**
5. 把里面的中文字改成别的，再跑一次

**过关**：不看笔记，能自己打开终端 → `cd` 到本目录 → `python week0\day01_hello.py` → 看到输出。

### Day B · 跑自检 + 做诊断 + 建仓库（约 2 小时）

1. 终端里跑 `python check_env.py`，四项全 PASS
2. 填 `diagnostic.md` 里的 10 道题（**不许查资料，写不出来就跳过**）
3. 按评分表确定起点，写进 `diagnostic.md` 最后一栏
4. 注册 GitHub → 建仓库 → 第一次 push（命令见下方「Day B 命令」）

### Day C · 补做手册 D2–D3（约 2 小时）

变量与计算、`input()` 与 f-string。跳到手册原文照做，代码存到 `week0\` 下。

---

## 四、每天 2 小时怎么切

| 时段 | 时长 | 干什么 |
|---|---|---|
| 开头 | 15 min | **合上所有资料**，凭记忆把昨天的代码重写一遍 |
| 中段 | 30 min | 看教程，**只看到能动手为止**，不要一口气看完 |
| 主体 | 65 min | 写代码。写不出就查，查不到问 AI，但必须自己敲 |
| 收尾 | 10 min | 填 `log\每日记录.md`：做了什么、卡在哪、明天第一件事 |

三条硬规则：**开头 15 分钟不能省** · **别连续坐 2 小时** · **每周留一天完全不学**。

---

## 五、命令速查

```bash
python --version            看 Python 版本
python 文件名.py             运行一个 py 文件
python                      进入交互模式（出现 >>> ，退出输入 exit()）
cd 目录                     切换目录
dir                         看当前目录有什么

git status                  看改了哪些文件
git add .                   把改动放进暂存区
git commit -m "说明"         提交一次
git log --oneline           看提交历史
```

> Git 装完要**新开一个终端窗口**才能直接敲 `git`，老窗口还认不到。

---

## 六、Day B 命令（GitHub 第一次 push）

```bash
# 1. 配身份（换成你自己的名字和 GitHub 邮箱）
git config --global user.name "你的名字"
git config --global user.email "你的GitHub邮箱"

# 2. 提交本目录
git add .
git commit -m "第0周：环境就绪 + 诊断"

# 3. 连到 GitHub（先在网页上建一个空仓库，别勾 README）
git remote add origin https://github.com/你的用户名/仓库名.git
git branch -M main
git push -u origin main
```

---

## 七、目录说明

```
python-learn\
├─ START_HERE.md          ← **从这份开始**：14 件事的进度表，一件一件打勾
├─ README.md              本文件（参考资料，不用逐行读）
├─ check_env.py           环境自检脚本
├─ diagnostic.md          10 题诊断（填完再决定从哪周开始）
├─ week0\
│  └─ day01_hello.py      Day 1 示例：跑通就是环境齐了
└─ log\
   └─ 每日记录.md          每天的 10 分钟收尾写这里
```

---

## 八、第 0 周过关清单

- [ ] `python --version` 显示 3.11 以上
- [ ] `python week0\day01_hello.py` 能输出中文，不乱码
- [ ] `python check_env.py` 四项全 PASS
- [ ] `git --version` 显示 2.x（新终端）
- [ ] VS Code 能打开本目录，`Python` + `Pylance` 已装
- [ ] 10 题诊断做完，起点已确定
- [ ] GitHub 上有第一个提交

打勾 7 项 = 第 0 周结束，进手册第 0 周 Day 2。
