from setuptools import setup

setup(name='tudais',
      version='0.1',
      description='Supplemental material for the lecture Angewandte '
                  'Intelligente Signalverarbeitung at TU Dresden',
      url='http://github.com/TUD-STKS/tud-ais-package',
      author='Simon Stone',
      author_email='simon.stone@tu-dresden.de',
      license='MIT',
      packages=['tudais'],
      include_package_data=True,
      install_requires=[
          'jupyterlab',
          'pandas',
          'scikit-learn',
          'tudthemes'
      ],
      entry_points={
          'console_scripts': [
              'tud-ais = tudais.__main__:start_jupyter_server',
          ]
      }
      )
