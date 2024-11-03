from matplotlib.transforms import Affine2D
import matplotlib.patches as patches
from matplotlib.axes import Axes
from typing import Literal

from .markers import taralib_paths

def add_background(ax : Axes, 
                   image : Literal['cat', 'pawprint', 'teacup', 'teabag'], 
                   loc: tuple[float, float] = (0.975, 0.025), 
                   scale:float = 0.1,
                   horizontalalignment : Literal['left', 'center', 'right'] = 'right',
                   verticalalignment : Literal['top', 'center', 'bottom'] = 'bottom',
                   linewidth : float = 2,
                   facecolor : str = 'none',
                   edgecolor : str = 'TPLBlue',
                   alpha : float = 0.4,
                   zorder : int = -1,
                   keep_aspect : bool = True,
                   **kwargs
                   ) -> None:
    
    
    path = taralib_paths[image]
    path = path.transformed(Affine2D().scale(scale, scale))
    # paths come centered
    # we need to align them properly
    bbox = path.get_extents()
    original_aspect = bbox.width / bbox.height
    
    if horizontalalignment == 'left':
        path = path.transformed(Affine2D().translate(+bbox.width/2, 0))
    elif horizontalalignment == 'right':
        path = path.transformed(Affine2D().translate(-bbox.width/2, 0))
    
    if verticalalignment == 'top':
        path = path.transformed(Affine2D().translate(0, -bbox.height/2))
    elif verticalalignment == 'bottom':
        path = path.transformed(Affine2D().translate(0, +bbox.height/2))
    
    path = path.transformed(Affine2D().translate(*loc))
    
    ## This is a hack to keep the aspect ratio
    ## The only way I can think of is to transform the path
    ## to axes coordinates, get the aspect ratio, and then
    ## transform it back to figure coordinates
    
    if keep_aspect:
        path = path.transformed(ax.transAxes)
        trans_bbox = path.get_extents()
        trans_aspect = trans_bbox.width / trans_bbox.height
        path = path.transformed(ax.transAxes.inverted())
        path = path.transformed(Affine2D().scale(1, trans_aspect/original_aspect))
    
    patch = patches.PathPatch(path, 
                              facecolor=facecolor, 
                              lw = linewidth,
                              edgecolor = edgecolor,
                              alpha = alpha,
                              **kwargs)
    
    patch.set_transform(ax.transAxes)
    patch.zorder = zorder
    
    ax.add_patch(patch)
