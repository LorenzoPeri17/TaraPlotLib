__all__ = ['add_background'] # type: ignore

from cycler import cycler
from matplotlib import rcParams
from matplotlib.font_manager import fontManager
from matplotlib.colors import to_rgba

from matplotlib.lines import Line2D

from .src.colors import _add_colors_to_mpl
from .src.markers import (
    _add_markers_to_mpl,
    taralib_paths
)
from .src.background import add_background

import warnings

# Markers have been added through a terrible hack
# that throws a warning. Let's just hide it.
warnings.filterwarnings("ignore")

_add_colors_to_mpl()
_add_markers_to_mpl()

rcParams['axes.prop_cycle'] = cycler(
    color=[
    to_rgba('#43978D', 0.5),
    to_rgba('#F9AD6A', 0.5),
    to_rgba('#264D59', 0.5),
    to_rgba('#813563', 0.5),
    ],
    marker = [
    'teacup',
    'teabag',
    'cat',
    'pawprint',
    ],
    markeredgecolor = [
    '#43978D',
    '#F9AD6A',
    '#264D59',
    '#813563',
    ])

rcParams["axes.labelpad"] = 1.5
rcParams["axes.formatter.useoffset"] = False
rcParams["axes.axisbelow"] = False
rcParams["axes.unicode_minus"] = False

rcParams["lines.marker"] = 'teacup'
rcParams["lines.markersize"] = 15
rcParams["lines.linestyle"] = (0, (5, 15))
rcParams["lines.linewidth"] = 1
rcParams["lines.markeredgewidth"] = 1.2
rcParams["markers.fillstyle"] = 'none'

rcParams["font.family"] = "serif"
if "Apple Chancery" in [f.name for f in fontManager.ttflist]:
    rcParams["font.serif"] = ["Apple Chancery"] + rcParams["font.serif"]
if "PilGi" in [f.name for f in fontManager.ttflist]:
    rcParams["font.serif"] = ["PilGi"] + rcParams["font.serif"]
rcParams["font.size"] = 14
rcParams["axes.labelsize"] = 19

rcParams['figure.autolayout'] = True
rcParams['image.cmap'] = 'crime-yoga'

## Set markevery for Line2D
# This is a hack to set the default markevery
# because it does not have an entry in rcParams

def _set_markevery(self: Line2D, every):
    if every is None:
        every = 0.1
    elif every == 'none':
        every = None
    self._markevery = every # type: ignore
    self.stale = True
    
def _get_markevery(self: Line2D):
    if self._markevery is not None and self.axes is None: # type: ignore
        return None
    return self._markevery # type: ignore
    
_set_markevery.__doc__ = Line2D.set_markevery.__doc__
_get_markevery.__doc__ = Line2D.get_markevery.__doc__
    
Line2D.set_markevery = _set_markevery # type: ignore
Line2D.get_markevery = _get_markevery # type: ignore
    