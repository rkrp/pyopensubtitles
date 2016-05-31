try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python wrapper for OpenSubtitles API and a CLI tool to download subtitles',
    'author': 'Krishna Ram Prakash R',
    'url': 'https://github.com/rkrp/pyopensubtitles',
    'download_url': 'https://github.com/rkrp/pyopensubtitles',
    'author_email': 'krp@gtux.in',
    'version': '0.1',
    'install_requires': [],
    'packages': ['pyopensubtitles'],
    'scripts': ['bin/fetchsubs.py'],
    'name': 'pyopensubtitles',
    'license' : 'GPLv3',
    'classifiers' : [
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
    ],
}

setup(**config)

