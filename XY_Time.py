#!/user/bin/python3
# -*- coding: utf-8 -*-

import pygal
from datetime import time

time_chart = pygal.TimeLine(x_label_rotation = 25)
time_chart.add("Serie", [
  (time(), 0),
  (time(6), 5),
  (time(8, 30), 12),
  (time(11, 59, 59), 4),
  (time(18), 10),
  (time(23, 30), -1),
])

time_chart.render_to_file('./image/xy_time.svg')


