#!/user/bin/python3
# -*- coding: utf-8 -*-

# Scatter Plot 散点图
import random

import pygal

scatter_plot_chart = pygal.XY(stroke=False)
scatter_plot_chart.title = "散点图"
list_a = []
list_b = []
list_c = []
for i in range(20):
    a = random.uniform(0,5)
    b = random.uniform(0,5)
    list_a.append((a,b))
for j in range(20):
    a = random.uniform(0,5)
    b = random.uniform(0,5)
    list_b.append((a,b))
for s in range(20):
    a = random.uniform(0,5)
    b = random.uniform(0,5)
    list_c.append((a,b))
scatter_plot_chart.add('A', list_a)
scatter_plot_chart.add('B', list_b)
scatter_plot_chart.add('C', list_c)
scatter_plot_chart.render_to_file('./image/xy_scatter_plot.svg')