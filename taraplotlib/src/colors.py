import matplotlib as mpl
from matplotlib import colors
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from matplotlib.colors import get_named_colors_mapping
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings("ignore")

def _add_colors_to_mpl() -> None:
    """
    Adds colors and colormaps to matplotlib
    """

    mpl_color_mapping = get_named_colors_mapping()

    mpl_color_mapping |= {
        'TPLBlue': '#264D59',
        'TPLTeal': '#43978D',
        'TPLYellow': '#F9E07F',
        'TPLOrange': '#F9AD6A',
        'TPLBrown': '#D46C4E',
        'TPLRed': '#FA425A',
        'TPLPurple': '#813563',
    }
    
    _TPLAncientRome_data = [
        '#264d59',
        '#357273',
        '#43978d',
        '#a2bd86',
        '#f9e07f'
    ]
    
    _TPLWarmTea_data = [
        '#813563',
        '#aa3d5e',
        '#d74659',
        '#db684c',
        '#de893e'
    ]
    
    _TPLCandleLight_data = [
        '#d46c4e',
        '#e78d5c',
        '#f9ad6a',
        '#f9c775',
        '#f9e07f'
    ]
    
    _TPLTaraTime_data = [
        '#a40160',
        '#833ab4',
        '#47578e',
        '#dd6826',
        '#fce645'
    ]
    
    _TPLNightWalk_data = [
        '#2e3652',
        '#364351',
        '#3f524f',
        '#a3a783',
        '#fff6b3'
    ]
    
    _TPLCrimeYoga_data = [
        '#472885',
        '#3d4e9c',
        '#6caccb',
        '#79cdc1',
        '#9fffd1'
    ]
    
    TPLAncientRome = LinearSegmentedColormap.from_list('ancient-rome', _TPLAncientRome_data)
    TPLWarmTea = LinearSegmentedColormap.from_list('warm-tea', _TPLWarmTea_data)
    TPLTaraTime = LinearSegmentedColormap.from_list('tara-time', _TPLTaraTime_data)
    TPLCandleLight = LinearSegmentedColormap.from_list('candle-light', _TPLCandleLight_data)
    TPLNightWalk = LinearSegmentedColormap.from_list('night-walk', _TPLNightWalk_data)
    TPLCrimeYoga = LinearSegmentedColormap.from_list('crime-yoga', _TPLCrimeYoga_data)
    
    TPLCycler = ListedColormap(
        [
            '#43978D', 
            '#F9AD6A',
            '#264D59',
            '#F9E07F',
            '#813563',
            '#D46C4E',
        ],
        name="TPLCycler",
    )
    
    for _cmap in [TPLAncientRome, TPLWarmTea, TPLTaraTime, TPLCandleLight, TPLNightWalk, TPLCrimeYoga, TPLCycler]:
        plt.colormaps.register(cmap=_cmap, force=True)


def get_hex(cmap_name: str, ncolors: int) -> list:
    """
    Get a list of hex values from a matplotlib colourmap. Works with all matplotlib colourmaps.
    """
    
    _add_colors_to_mpl()

    if "TPLCycler" in cmap_name:
        cw = [
            '#43978D', 
            '#F9AD6A',
            '#264D59',
            '#F9E07F',
            '#813563',
            '#D46C4E',
        ]
    else:
        cw = [
            colors.rgb2hex(mpl.colormaps[cmap_name](k / ncolors))
            for k in range(ncolors + 1)
        ]

    return cw
