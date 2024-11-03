from matplotlib import pyplot as plt
import numpy as np

from pathlib import Path

from taraplotlib import *

x = np.linspace(0, 1, 1000)
y = np.linspace(0, 1, 1000)

x, y = np.meshgrid(x, y)

z = np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y)

fig, ax = plt.subplots()

im = ax.pcolormesh(x, y, z)

add_background(ax, 'teacup', zorder=1, edgecolor='TPLYellow')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

plt.colorbar(im, ax=ax, label = 'z-axis')

fig.savefig(Path(__file__).with_suffix( ".png"))

plt.show()