# -*- coding: utf-8 -*-
"""
环境自检 —— 跑一遍，看装备齐不齐。

用法：python check_env.py
四项全 PASS 就说明第 0 周的环境部分完成了。
"""

import os
import shutil
import subprocess
import sys

PASS = []
FAIL = []


def title(text):
    print()
    print("=" * 50)
    print(text)
    print("=" * 50)


def check_python():
    title("1. Python")
    print("版本 :", sys.version.split()[0])
    print("路径 :", sys.executable)
    print("位数 :", "64 位" if sys.maxsize > 2 ** 32 else "32 位")
    if sys.version_info >= (3, 11):
        PASS.append("Python 3.11+")
    else:
        FAIL.append("Python 版本低于 3.11，建议升级")


def check_git():
    title("2. Git")
    git = shutil.which("git") or r"C:\Program Files\Git\cmd\git.exe"
    if not os.path.exists(git):
        print("没找到 git")
        FAIL.append("Git 未安装或不在 PATH（新开一个终端再试）")
        return
    try:
        out = subprocess.run(
            [git, "--version"], capture_output=True, text=True, timeout=10
        ).stdout.strip()
    except Exception as exc:  # noqa: BLE001
        print("调用 git 失败:", exc)
        FAIL.append("Git 无法执行")
        return
    print("版本 :", out)
    print("路径 :", git)
    PASS.append("Git")


def check_vscode():
    title("3. VS Code")
    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "AppData", "Local", "Programs", "Microsoft VS Code", "Code.exe"),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ]
    for path in candidates:
        if os.path.exists(path):
            print("路径 :", path)
            PASS.append("VS Code")
            return
    print("没找到 Code.exe")
    FAIL.append("VS Code 未安装")


def check_encoding():
    title("4. 中文编码")
    text = "中文测试：你好，世界 —— 这行不乱码就正常"
    print(text)
    if os.environ.get("PYTHONUTF8") == "1":
        print("UTF-8 模式 : 已开启（PYTHONUTF8=1）")
    else:
        print("UTF-8 模式 : 未开启（乱码的话设一个用户环境变量 PYTHONUTF8=1）")
    PASS.append("中文输出")


def main():
    check_python()
    check_git()
    check_vscode()
    check_encoding()

    title("结果")
    for item in PASS:
        print("  PASS  ", item)
    for item in FAIL:
        print("  FAIL  ", item)
    print()
    if FAIL:
        print("还有 {} 项没过，按上面的提示处理。".format(len(FAIL)))
    else:
        print("全部通过。环境这块可以不用管了，去写代码。")


if __name__ == "__main__":
    main()
