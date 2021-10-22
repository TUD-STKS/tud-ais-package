from setuptools import setup
import glob

setup(name='tud-ais',
      version='0.1.6',
      description='Supplemental material for the lecture Angewandte Intelligente Signalverarbeitung at TU Dresden',
      url='http://github.com/TUD-STKS/tud-ais-package',
      author='Simon Stone',
      author_email='simon.stone@tu-dresden.de',
      license='MIT',
      packages=['tud-ais'],
      include_package_data=True,
      install_requires=[
          'jupyterlab',
          'pandas',
          'scikit-learn',
      ],
      )
