from matplotlib import pyplot as plt
import numpy as np

from pathlib import Path

from taraplotlib import *

x = np.linspace(0, 10, 10)

fig, ax = plt.subplots()

ax.plot(x, x)

add_background(ax, 'cat')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

fig.savefig(Path(__file__).with_name( "single_line.png"))

plt.show()