pyopensubtitles
===============

Python wrapper for OpenSubtitles.org XMLRPC API 

A command line utility to download subtitles for movies and episodes of TV
shows from opensubtitles.org

Please do not forget to change the user agent in `settings.py` from the
default value to the one you obtain after signing up from [OpenSubtitles.org]
(https://trac.opensubtitles.org/projects/opensubtitles/wiki/DevReadFirst)

Usage
-----

    usage: fetchsubs.py [-h] show season episode

    positional arguments:
      show
      season
      episode

    optional arguments:
      -h, --help  show this help message and exit

For example,

    fetchsubs.py "Breaking Bad" 01 01


Credits
-------

Thanks to OpenSubtitles.org
