from matplotlib import pyplot as plt
import numpy as np

from pathlib import Path

from taraplotlib import *

x = np.linspace(0, 10, 100)
y = np.ones_like(x)

fig, ax = plt.subplots()

for i in range(4):
    ax.plot(x, x+2*i)

add_background(ax, 'cat')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

fig.savefig(Path(__file__).with_suffix( ".png"))

plt.show()