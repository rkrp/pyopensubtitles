#!/usr/bin/python2

from pyopensubtitles.pyopensubtitles import PyOpenSubtitles
from pyopensubtitles.exceptions import *
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('--mode', choices=['auto', 'manual'], default='auto')
    parser.add_argument('--season', type=int, help="season number")
    parser.add_argument('--episode', type=int, help="episode number")
    parser = parser.parse_args()

    pyos = PyOpenSubtitles()

    print "[*] Searching for subtitles.."

    if parser.mode == 'manual':
        try:
            title = parser.filename
            season = parser.season
            episode = parser.episode
        except AttributeError:
            pass

        results = pyos.search_subtitle(title, season, episode)
    else:
        try:
            metadata = pyos.guess_parameters(parser.filename)
        except GuessError:
            print "[-] Cannot guess video details. Please try manual mode"

        title = metadata['title']
        season = metadata['season'] if 'season' in metadata else None
        episode = metadata['episode'] if 'episode' in metadata else None

        results = pyos.search_subtitle(title, season, episode)

    num_results = len(results['data'])

    if num_results == 0:
        print "[-] No subtitles found"
        return 1

    print "[+] Found %d subtitles" %(len(results['data']))
    print "[*] Downloading Subtitle.."
    idsubtitlefile = results['data'][0]['IDSubtitleFile']
    filename = "%s.S%02dE%02d.srt" %(title, season, episode)
    filename = filename.replace(" ", ".")

    pyos.download_subtitle(idsubtitlefile, filename)

    print "[+] Subtitles saved as %s" %(filename)

if __name__ == '__main__':
    main()
