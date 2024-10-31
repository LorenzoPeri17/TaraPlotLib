from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D
from matplotlib.path import Path
from pathlib import Path as filePath
from svgpathtools import svg2paths
from svgpath2mpl import parse_path

_marker_svgs = {
        'cat' : "cat-silhouette-000000-original.svg",
        'pawprint' : "cat-footprint-silhouette-000000-original.svg",
        'teacup' : "cup-of-tea-silhouette-000000-original.svg",
        'teabag' : "tea-bags-silhouette-000000-original.svg",
    }

taralib_paths : dict[str, Path] = {}
for marker_name, marker_svg in _marker_svgs.items():
    # Load the SVG file and convert it to a path
    paths, _ = svg2paths(filePath(__file__).resolve().parents[1] / "assets" / marker_svg) # type: ignore
    marker_path = parse_path(paths[0].d())
    # Center the paths
    marker_bbox = marker_path.get_extents()
    marker_path = marker_path.transformed(Affine2D().translate(-marker_bbox.width/2, -marker_bbox.height/2))
    # Scale the path to unity
    _scale = max(marker_bbox.width, marker_bbox.height)
    marker_path = marker_path.transformed(Affine2D().scale(1/_scale, 1/_scale))
    if marker_name == 'cat':
        # The cat is upside down
        marker_path = marker_path.transformed(Affine2D().rotate_deg(180))
    taralib_paths[marker_name] = marker_path

def _add_markers_to_mpl() -> None:

    for marker_name, marker_path in taralib_paths.items():
        # Add the marker to the named markers
        MarkerStyle.markers[marker_name] = marker_name
        # Capture marker_path as argument of lambda to avoid issues with late binding
        setattr(MarkerStyle, f'_set_{marker_name}', lambda self, path=marker_path: self._set_custom_marker(path))
        
    return
