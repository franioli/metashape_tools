from metashape_tools.menu import register_menu
from metashape_tools.utils import check_compatibility

check_compatibility(["2.0", "2.1", "2.2", "2.3"])


if __name__ == "__main__":
    register_menu()
