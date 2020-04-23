#!/user/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
import pygal

data_chart = pygal.Line(x_label_rotation=20)
data_chart.x_labels = map(lambda d : d.strftime('%Y-%m-%d'),[
    datetime(2020,1,2),
    datetime(2020,2,12),
    datetime(2020,3,2),
    datetime(2020,4,12),
])
data_chart.add('Visits',[300,500,600,520,677])

data_chart.render_to_file('./image/line_time.svg')