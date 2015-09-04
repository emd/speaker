try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'speaker',
    'version': '0.1',
    'packages': ['speaker'],
    'package_data': {'speaker': ['speaker/calibration_data/*.csv']},
    'install_requires': ['numpy', 'scipy', 'nose'],
    'author': 'Evan M. Davis',
    'author_email': 'emd@mit.edu',
    'url': '',
    'description': 'Python tools for characterizing speaker sound waves.'
}

setup(**config)
