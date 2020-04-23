#!/user/bin/python3
# -*- coding: utf-8 -*-

# Donut 圆环图

import pygal

# inner_radius 内半径
donut_chart = pygal.Pie(inner_radius=.75)
# 内半径越大 圆环图就越像一个环 .4 -> .75 .75的时候就很像一个环
donut_chart.title = 'Browser usage in February 2012 (in %)'
donut_chart.add('IE', 19.5)
donut_chart.add('Firefox', 36.6)
donut_chart.add('Chrome', 36.3)
donut_chart.add('Safari', 4.5)
donut_chart.add('Opera', 2.3)
donut_chart.render_to_file('./image/pie_donut.svg')