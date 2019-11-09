# -*- coding: utf-8 -*-

R"""
子プロセスのfork4(Pythonからの入力をLinux側でパイプ)
"""

import subprocess


def run_sed_A2a(line):
    R"""
    大文字Aを小文字aへ変換するsedコマンド呼出
    :param      line:   sedへ入力する文字列
    :return:    sedの子プロセス
    """
    proc = subprocess.Popen(
        ['sed', '-e', 's/A/a/g'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )  # Popen

    # 変換元文字列を標準入力へリダイレクト
    proc.stdin.write(line)
    proc.stdin.flush()

    return proc


# 'Arkansas'が'arkansas'へ変換される
out, _ = run_sed_A2a(line=b'Arkansas').communicate()
print(out)
