# -*- coding: utf-8 -*-

R"""
日付時刻とタイムゾーンを活用する
"""

from datetime import datetime

import pytz

# 現在時刻を取得
now = datetime.now()
print(now)

# まずは東京の現在時刻をUTC時刻へ変換
tokyo_tz = pytz.timezone(zone='Asia/Tokyo')
tokyo_tm = tokyo_tz.localize(dt=now)
utc_tm = pytz.utc.normalize(dt=tokyo_tm.astimezone(pytz.utc))
print(utc_tm)

# UTC時刻をベルリンの現地時間へ変換
berlin_tz = pytz.timezone(zone='Europe/Berlin')
berlin_tm = berlin_tz.normalize(dt=utc_tm.astimezone(berlin_tz))
print(berlin_tm)
