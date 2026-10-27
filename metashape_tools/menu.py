from __future__ import annotations

import importlib
import sys
from collections.abc import Callable

import Metashape

from metashape_tools import (
    calibration_tools,
    camera_tools,
    chunk_tools,
    fiducial_tools,
    incremental_alignment,
    io_tools,
    marker_tools,
    tie_points_tools,
    triangulation,
)

_menu_labels: list[str] = []


def _add(label: str, func: Callable[[], None]) -> None:
    Metashape.app.addMenuItem(label, func)
    _menu_labels.append(label)


def register_menu() -> None:
    """Register all Custom/* menu items."""
    # Tie points
    _add(
        "Custom/TiePoints/Show Statistics...", tie_points_tools.tiepoint_stats_dialog
    )
    _add(
        "Custom/TiePoints/Filter by Covariance...",
        tie_points_tools.tiepoint_covariance_filter_dialog,
    )
    _add(
        "Custom/TiePoints/Disable Outside Region...",
        tie_points_tools.tiepoints_disable_outside_region_dialog,
    )

    # Cameras
    _add(
        "Custom/Cameras/Remove duplicates...",
        camera_tools.remove_duplicate_cameras_dialog,
    )
    _add(
        "Custom/Cameras/Clear camera source coordinates...",
        camera_tools.clear_camera_coordinates_dialog,
    )
    _add(
        "Custom/Cameras/Write estimated to source...",
        camera_tools.write_estimated_to_source_dialog,
    )
    _add(
        "Custom/Cameras/Export selected images...",
        camera_tools.export_selected_images_dialog,
    )
    _add(
        "Custom/Cameras/Export reference CSV...",
        camera_tools.export_camera_reference_dialog,
    )

    # Markers
    _add(
        "Custom/Markers/Import projections...",
        marker_tools.import_markers_images_dialog,
    )
    _add(
        "Custom/Markers/Export projections...",
        marker_tools.export_markers_images_dialog,
    )
    _add(
        "Custom/Markers/Remove blue flags...",
        marker_tools.remove_marker_blue_flags_dialog,
    )

    # Incremental alignment
    _add(
        "Custom/Incremental Alignment/Align unaligned...",
        incremental_alignment.incremental_alignment_dialog,
    )
    _add(
        "Custom/Incremental Alignment/Realign selected...",
        incremental_alignment.realign_selected_cameras_dialog,
    )
    _add(
        "Custom/Incremental Alignment/Export unaligned list...",
        incremental_alignment.export_unaligned_list_dialog,
    )
    _add(
        "Custom/Incremental Alignment/Transfer oriented from chunk...",
        incremental_alignment.transfer_oriented_cameras_dialog,
    )

    # Chunk
    _add(
        "Custom/Chunk/Expand region...",
        chunk_tools.expand_region_dialog,
    )

    # FIducials
    _add(
        "Custom/Fiducials/Import from CSV...",
        fiducial_tools.import_fiducials_from_file_dialog,
    )
    _add(
        "Custom/Fiducials/Add manually...", fiducial_tools.add_fiducial_manual_dialog
    )

    # IO / export-import
    _add(
        "Custom/IO/Export sparse points...", io_tools.export_sparse_dialog
    )
    _add(
        "Custom/IO/Project from Bundler...", io_tools.import_from_bundler_dialog
    )

    # Other tools can be added here following the same pattern
    _add(
        "Custom/Other/Convert OpenCV to COLMAP...",
        calibration_tools.convert_opencv_to_colmap,
    )
    _add(
        "Custom/Other/Triangulate points from CSV...", triangulation.triangulate_points
    )

    _add("Custom/Other/Reload tools", reload_tools)

    print("Custom tools registered (Custom/*).")
    print("")
    print(
        "NOTE: this package is in early development and tools may not work as expected. Please report any issues to the developers."
    )


def reload_tools() -> None:
    """Reload all metashape_tools modules and re-register the menu.

    Menu items hold references to the old function objects, so they are
    removed and added again after the reload.
    """
    for label in _menu_labels:
        Metashape.app.removeMenuItem(label)
    _menu_labels.clear()

    # Reload dependencies first (utils), then the rest, then this module.
    names = sorted(
        (n for n in sys.modules if n.startswith("metashape_tools.") and n != __name__),
        key=lambda n: (n != "metashape_tools.utils", n),
    )
    for name in names:
        importlib.reload(sys.modules[name])
        print("Reloaded {}".format(name))

    menu = importlib.reload(sys.modules[__name__])
    menu.register_menu()
    print("Tools reloaded.")
