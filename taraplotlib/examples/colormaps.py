'''
Code inspired by the matplotlib colormaps example.
https://matplotlib.org/stable/users/explain/colors/colormaps.html
'''

from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

from pathlib import Path

from taraplotlib import *

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

cmap_list = [
    'ancient-rome',
    'warm-tea',
    'tara-time',
    'candle-light',
    'night-walk',
    'crime-yoga',
]

nrows = len(cmap_list)
fig, axs = plt.subplots(nrows=nrows)
axs[0].set_title(f'taraplotlib colormaps')

for ax, name in zip(axs, cmap_list):
    ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
    ax.text(-0.01, 0.5, name, va='center', ha='right',
            transform=ax.transAxes)
    ax.set_axis_off()

fig.savefig(Path(__file__).with_suffix( ".png"))

plt.show()
