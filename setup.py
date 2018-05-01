from setuptools import setup, find_packages
import sys

long_description = open('README.md', 'r').read()

setup(name='oscc-check',
      version='0.0.1',
      url = 'https://github.com/PolySync/oscc-check',
      author = 'Shea Newton',
      author_email = 'snewton@polysync.io',
      maintainer = 'PolySync Technologies',
      maintainer_email = 'help@polysync.io',
      description = 'Check that your vehcile and the installed OSCC are in a good state.',
      long_description = long_description,
      download_url = 'https://github.com/PolySync/oscc-check',
      packages = ["oscccan"],
      license = 'MIT',
      install_requires = [
          'colorama',
          'docopt',
          'python-can',
        ],
      classifiers = [
        'Environment :: Console',
        'License :: MIT License',
        'Natural Language :: English',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        ],
    )
