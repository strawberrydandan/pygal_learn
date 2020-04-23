#!/user/bin/python3
# -*- coding: utf-8 -*-

# Histogram 直方图

import pygal

hist = pygal.Histogram()
hist.title = 'Data Show This ..'
hist.add('Wide bars', [(5, 0, 10), (4, 5, 13), (2, 0, 15)])
hist.add('Narrow bars',  [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)])
hist.render_to_file('./image/histogram_basic.svg')