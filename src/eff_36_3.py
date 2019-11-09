# -*- coding: utf-8 -*-

R"""
子プロセスのfork3(子プロセス並列実行)
"""

import subprocess
from time import time


def run_sleep(period):
    R"""
    指定した時間だけ待機する子プロセスを返す
    :param      period: 子プロセスが待機する秒数
    :return:    sleepを設定した子プロセス
    """
    proc = subprocess.Popen(args=['sleep', str(period)])

    return proc


start = time()

# 1秒間待機する子プロセスを10個生成
procs = [run_sleep(1.0) for _ in range(10)]

# 10個の子プロセスを一斉に実行
for p in procs:
    p.communicate()

end = time()

# 並列実行なので、10秒ではなく約1秒で終わる
print('Finished in {} seconds'.format(end - start))
