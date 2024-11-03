from matplotlib import pyplot as plt
import numpy as np

from pathlib import Path
from matplotlib.colors import to_rgba

from taraplotlib import *

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()

ax.plot(x, x)

add_background(ax, 'cat')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

fig.savefig(Path(__file__).with_suffix( ".png"))

plt.show()