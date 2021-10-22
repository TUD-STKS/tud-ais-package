if __name__ == '__main__':
    import os
    from pathlib import Path
    pkg_root = Path(os.path.dirname(os.path.realpath(__file__)))
    os.system('jupyter notebook --notebook-dir=' + str(pkg_root / Path('notebooks')))

