import pygal

multi_series_pie_chart = pygal.Pie()


multi_series_pie_chart.title = 'Browser usage by version in February 2012 (in %)'
multi_series_pie_chart.add('IE', [5.7, 10.2, 2.6, 1])
multi_series_pie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
multi_series_pie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
multi_series_pie_chart.add('Safari', [4.4, .1])
multi_series_pie_chart.add('Opera', [.1, 1.6, .1, .5])
multi_series_pie_chart.render_to_file('./image/pie_multi_series_pie.svg')