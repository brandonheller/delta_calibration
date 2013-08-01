#!/usr/bin/env python
import math

lt1 = 0.99999  # less than one

def floatrange(start, stop, divs):
    return [start + ((stop - start) * float(i)/divs) for i in range(divs + 1)]

def list_diff(l1, l2):
    return [a - l2[i] for i, a in enumerate(l1)]

def circle(x):
    """Return y value on unit circle.

    x: in [0,1], x distance
    """
    if x > lt1:
        return 0
    else:
        return math.sqrt(1.0-x*x)

def parabola(x):
    """Return y value on unit parabola.

    x: in [0,1], x distance
    """
    return 1 - x*x

def interp(x, fcn, divs):
    """Return linear-interpolated values.

    x: in [0,1], x distance on unit circle
    divs: number of divisions
    """
    assert divs != 0
    prev_x = math.floor(x*divs) / divs
    next_x = math.ceil(x*divs) / divs
    if prev_x == next_x:
        return fcn(x)
    assert prev_x != next_x
    # Slope
    m = (fcn(next_x) - fcn(prev_x)) / (next_x - prev_x) 
    # Intercept
    b = fcn(prev_x)
    return m * (x-prev_x) + b
