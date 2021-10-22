import os
from pathlib import Path


def start_jupyter_server():
    pkg_root = Path(os.path.dirname(os.path.realpath(__file__)))
    os.system('jupyter notebook --notebook-dir=' + str(pkg_root / Path('../tud-ais/notebooks')))


if __name__ == '__main__':
    start_jupyter_server()
