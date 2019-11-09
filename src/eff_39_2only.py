# -*- coding: utf-8 -*-

R"""
ブロッキングキューによるスレッド間の連携
"""

from threading import Lock, Thread

from queue import Queue

# サーバ側とクライアント側それぞれのキューを用意
server_queue = Queue()
client_queue = Queue()

# print時の排他用ロック
lock = Lock()


def sync_print(message):
    R"""
    サーバ側・クライアント側で表示が壊れないよう、同期する
    :param  message:    表示するオブジェクト
    """
    with lock:
        print(message)


def server():
    R"""
    TCP/IP通信のサーバ側コネクション確立シーケンスを模した関数
    """
    sync_print('Server accepting.')
    sync_print('Server: GET {}'.format(server_queue.get()))
    sync_print('Server: PUT syn+ack')
    client_queue.put(item='syn+ack')
    sync_print('Server: GET {}'.format(server_queue.get()))
    sync_print('Server done.')


def client():
    R"""
    サーバ側と同じく、クライアント側の確立シーケンスを模した関数
    """
    sync_print('Client connecting.')
    sync_print('Client: PUT syn')
    server_queue.put(item='syn')
    sync_print('Client: GET {}'.format(client_queue.get()))
    sync_print('Client: PUT ack')
    server_queue.put(item='ack')
    sync_print('Client done.')


# サーバ側は別スレッドとして起動
server_thread = Thread(target=server)
server_thread.start()

# メインスレッドがクライアント側処理を行う
client()
server_thread.join()
sync_print('Connection established.')

# サーバ側をメインスレッドにしても、ちゃんとシーケンス通りに動く
client_thread = Thread(target=client)
client_thread.start()

server()
client_thread.join()
sync_print('Connection established.')
