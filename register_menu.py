import sys
from pathlib import Path

# Make metashape_tools importable when Metashape runs this file from the
# startup scripts folder (also resolves symlinks back to the repository).
_root = str(Path(globals().get("__file__", ".")).resolve().parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from metashape_tools.menu import register_menu  # noqa: E402
from metashape_tools.utils import check_compatibility  # noqa: E402

check_compatibility(["2.0", "2.1", "2.2", "2.3"])
register_menu()
