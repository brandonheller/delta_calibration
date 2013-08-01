#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

from delta_error import floatrange, circle, parabola, interp, list_diff

plotted_divs = 1000
measured_divs_max = 10

FCN_COLOR_LIST = [
    (circle, 'r'),
    (parabola, 'b'),
]

xs = floatrange(0, 1, plotted_divs)

for y_fcn, color in FCN_COLOR_LIST:

    div_xs = []
    max_error_ys = []
    for measured_divs in range(1, measured_divs_max + 1):
        div_xs.append(measured_divs)
        ys_orig = [y_fcn(x) for x in xs]
        ys_interp = [interp(x, y_fcn, measured_divs) for x in xs]
        ys_error = list_diff(ys_orig, ys_interp)
        max_error_ys.append(max(ys_error))

    line, = plt.plot(div_xs, max_error_ys, color + '-', linewidth=2)

#plt.show()
plt.savefig("max_error.png")
