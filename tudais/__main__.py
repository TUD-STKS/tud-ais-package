import os
from pathlib import Path
import tudthemes


def get_notebook_dir():
    """
    Returns a string containing the path to the notebook directory
    """
    pkg_root = Path(os.path.dirname(__file__))
    return str(pkg_root / Path('notebooks'))


def start_jupyter_server():
    """
    Start a Jupyter server with notebook theming
    """
    pkg_root = Path(os.path.dirname(__file__))
    notebook_dir = get_notebook_dir()
    tudthemes.start_notebook(theme_select='bright', notebook_dir=notebook_dir)


if __name__ == '__main__':
    start_jupyter_server()
