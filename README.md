# Metashape-tools

Collection of python scripts for Metashape.

## Use the scripts in Metashape

### 1. Get the code

Clone the repository:

```bash
git clone <repository-url> metashape_tools
```

or download it as a zip from GitHub (Code → Download ZIP) and extract it.

### 2. Load the scripts

Choose one of the two options.

**Option A: load automatically at every start.** Copy `register_menu.py` and the `metashape_tools/` folder into Metashape's startup scripts folder (create the `scripts` folder if it does not exist):

| OS      | Folder                                                    |
| ------- | --------------------------------------------------------- |
| Linux   | `~/.local/share/Agisoft/Metashape Pro/scripts`            |
| Windows | `%LOCALAPPDATA%\Agisoft\Metashape Pro\scripts`            |
| macOS   | `~/Library/Application Support/Agisoft/Metashape Pro/scripts` |

Restart Metashape. All the tools are registered when it starts.

**Option B: load on demand.** Keep the repository where it is. In Metashape, open `Tools → Run Script...`, select `register_menu.py` and run it. Repeat after each restart.

> The `metashape_tools/` folder must be importable by Metashape's Python. If you get `ModuleNotFoundError: metashape_tools`, check the Console for the paths it searched and place the folder in one of them.

### 3. Use the tools

The tools appear in the new **Custom** menu, grouped by topic:

- `Custom/TiePoints`: statistics, covariance filter, disable outside region
- `Custom/Cameras`: remove duplicates, source coordinates, export images and reference
- `Custom/Markers`: import/export projections, remove blue flags
- `Custom/Incremental Alignment`: align unaligned, realign selected, transfer oriented cameras
- `Custom/Chunk`, `Custom/Fiducials`, `Custom/IO`, `Custom/Other`: remaining utilities

Several tools (e.g. `Remove blue flags`) work on the current selection when there is one, and on everything otherwise. Operations that change the project ask for confirmation first, and their log is written to the Console.

Note: if you make any edit to the code, use `Custom/Other/Reload tools` to apply the changes without restarting Metashape.

## Structure
```
metashape_scripts/
  README.md
  LICENSE
  register_menu.py                # Entry point to register menu in Metashape GUI
  metashape_tools/                # Python package (importable)
    tie_points_tools.py           # tie points stats + filters + bbox removal
    camera_tools.py               # camera utilities (keep existing, cleaned)
    chunk_tools.py                # generic chunk utilities
    markers_tools.py              # markers import/export + triangulation helpers
    incremental_alignment.py      # incremental alignment + transfer-oriented
    fiducials.py                  # Helpers for fiducial markers import
```
    
## Use Metashape as external module

### Create Environment with anaconda

Download the [current .whl file](https://www.agisoft.com/downloads/installer/) and install it following [these instructions](https://agisoft.freshdesk.com/support/solutions/articles/31000148930-how-to-install-metashape-stand-alone-python-module) (using the name of the .whl file that you downloaded).

```bash
conda create -n metashape python=3.10
conda activate metashape
pip3 install Metashape-"XX".whl
pip3 install -r requirements.txt
```

### License

Metashape license: You need a license (and associated license file) for Metashape. The easiest way to get the license file, is by installing the Metashape Professional Edition GUI software (distinct from the Python module) and registering it following the prompts in the software (you need to purchase a license first). Once you have a license file (whether a node-locked or floating license), you need to set the agisoft_LICENSE environment variable (search onilne for instructions for your OS; look for how to permanently set it) to the path to the folder containing the license file (metashape.lic).

With Linux (Ubuntu 22.04), to permanently setup agisoft_LICENSE environment variable for floating license, modify your .bashrc file:

```bash
sudo nano ~/.bashrc
```

add the line (replace port and address with your values)

```bash
export agisoft_LICENSE="port"@"address"
```

```bash
source ~/.bashrc
```

Check if the new environmental variable is present:

```bash
printenv | grep agisoft
```

Refer to [this guide](https://agisoft.freshdesk.com/support/solutions/articles/31000169378--metashape-2-x-linking-client-machine-to-the-license-server).

### Install external modules in Metashape built-in pyhton environment

Follow the official guide [https://agisoft.freshdesk.com/support/solutions/articles/31000136860-how-to-install-external-python-module-to-metashape-professional-package](https://agisoft.freshdesk.com/support/solutions/articles/31000136860-how-to-install-external-python-module-to-metashape-professional-package)

For Linux:

```bash
./metashape-pro/python/bin/python3.8 -m pip install "python_module_name"
```

### Issues

##### Reach Python Console

In Metashape app, if Reach Python Console does not work and gives the following error

```bash
Failed to import qtconsole.inprocess: libffi.so.6: cannot open shared object file: No such file or directory
Construction of rich console failed - using simple console
```

You need to manually install libffi6 with

```bash
wget https://mirrors.kernel.org/ubuntu/pool/main/libf/libffi/libffi6_3.2.1-8_amd64.deb
sudo apt install ./libffi6_3.2.1-8_amd64.deb
```
