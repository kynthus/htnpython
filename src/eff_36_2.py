# -*- coding: utf-8 -*-

R"""
子プロセスのfork2(親プロセスによるポーリング)
"""

import subprocess
from time import sleep

# 子プロセスは1秒間待つ
proc = subprocess.Popen(args=['sleep', '1.0'])

# 親プロセスは子プロセスが終わるまで0.2秒周期でメッセージを表示
while proc.poll() is None:
    print('Waiting child process...')
    sleep(0.2)
