#!/user/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime

# 时间：精确到秒
import pygal

datatime_chart = pygal.DateTimeLine(
    # x_label_rotation 与x轴的角度
    x_label_rotation=35,
    truncate_label=-1,
    x_value_formatter=lambda dt: dt.strftime('%d, %b %Y at %I:%M:%S %p'))

datatime_chart.add("Serie", [
    (datetime(2013, 1, 2, 12, 0), 300),
    (datetime(2013, 1, 12, 14, 30, 45), 412),
    (datetime(2013, 2, 2, 6), 823),
    (datetime(2013, 2, 22, 9, 45), 672)
])

datatime_chart.render_to_file('./image/xy_datatime.svg')