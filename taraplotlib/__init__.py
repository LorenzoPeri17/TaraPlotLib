__all__ = ['add_background'] # type: ignore

from cycler import cycler
from matplotlib import rcParams
from matplotlib.font_manager import fontManager

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
    '#43978D', 
    '#F9AD6A',
    '#264D59',
    '#813563',
    ],
    marker = [
    'teacup',
    'teabag',
    'cat',
    'pawprint',
    ])

rcParams["axes.labelpad"] = 1.5
rcParams["axes.formatter.useoffset"] = False
rcParams["axes.axisbelow"] = False
rcParams["axes.unicode_minus"] = False

rcParams["lines.marker"] = 'teacup'
rcParams["lines.markersize"] = 15
rcParams["lines.linestyle"] = 'none'
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