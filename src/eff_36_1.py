# -*- coding: utf-8 -*-

R"""
子プロセスのfork1(Linuxのみ)
"""

import subprocess

# echoコマンドを子プロセスとして起動
proc = subprocess.Popen(
    args=['echo', 'このメッセージはシェルにより出力される.'],
    stdout=subprocess.PIPE,
)  # Popen

# 出力結果を受け取り、標準出力をUTF-8で表示
out, _ = proc.communicate()
print(out.decode('utf-8'))
