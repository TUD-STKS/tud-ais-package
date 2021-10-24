import os
from pathlib import Path


def start_jupyter_server():
    pkg_root = Path(os.path.dirname(os.path.realpath(__file__)))
    notebook_dir = str(pkg_root / Path('notebooks'))
    os.system('jupyter notebook --notebook-dir=' + notebook_dir)


if __name__ == '__main__':
    start_jupyter_server()
