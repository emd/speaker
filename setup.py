try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'speaker',
    'version': '0.1',
    'packages': ['speaker'],
    'install_requires': ['numpy, matplotlib, scipy, nose'],
    'author': 'Evan M. Davis',
    'author_email': 'emd@mit.edu',
    'url': '',
    'description': 'Python tools for characterizing speaker sound waves.'
}

setup(**config)
