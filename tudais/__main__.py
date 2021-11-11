import os
from pathlib import Path
import tudthemes

def start_jupyter_server():
    pkg_root = Path(os.path.dirname(__file__))
    notebook_dir = str(pkg_root / Path('notebooks'))
    custom_style_dir = tudthemes.get_address('bright')
    os.environ["JUPYTER_CONFIG_DIR"] = custom_style_dir
    os.system('jupyter notebook --notebook-dir=' + notebook_dir)

if __name__ == '__main__':
    start_jupyter_server()