#!/user/bin/python3
# -*- coding: utf-8 -*-

# Data：日期精确到日

import pygal
from datetime import date

data_chart = pygal.DateLine(x_label_rotation=25)
data_chart.x_labels =\
    [
    date(2013, 1, 1),
    date(2013, 7, 1),
    date(2014, 1, 1),
    date(2014, 7, 1),
    date(2015, 1, 1),
    date(2015, 7, 1)
    ]

data_chart.add("Serie",
    [(date(2013, 1, 2), 213),
    (date(2013, 8, 2), 281),
    (date(2014, 12, 7), 198),
    (date(2015, 3, 21), 120)])

data_chart.render_to_file('./image/xy_data.svg')