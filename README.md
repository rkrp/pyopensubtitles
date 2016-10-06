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

####Automatic Downloading of subtitles from movie/episode filename

    fetchsubs.py The.Secret.Life.of.Walter.Mitty.2013.720p.BluRay.x264.YIFY.mp4

This will download 

    usage: fetchsubs.py [-h] [--mode {auto,manual}] [--season SEASON]
                        [--episode EPISODE]
                        filename

    positional arguments:
      filename

    optional arguments:
      -h, --help            show this help message and exit
      --mode {auto,manual}
      --season SEASON       season number
      --episode EPISODE     episode number



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
