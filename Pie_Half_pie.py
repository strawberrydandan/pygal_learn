#!/user/bin/python3
# -*- coding: utf-8 -*-
import pygal

half_pie_chart = pygal.Pie(half_pie=True)
half_pie_chart.title = 'Browser usage in February 2012 (in %)'
half_pie_chart.add('IE', 19.5)
half_pie_chart.add('Firefox', 36.6)
half_pie_chart.add('Chrome', 36.3)
half_pie_chart.add('Safari', 4.5)
half_pie_chart.add('Opera', 2.3)
half_pie_chart.render_to_file('./image/pie_half_pie.svg')