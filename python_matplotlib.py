#!/usr/bin/env python

try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.rcParams['backend'] = 'Qt5Agg'
    import matplotlib.pyplot as plt


