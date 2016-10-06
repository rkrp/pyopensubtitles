#!/usr/bin/python2

from pyopensubtitles.pyopensubtitles import PyOpenSubtitles
from pyopensubtitles.exceptions import *
import argparse

def autofetch(pyos, parser):
    try:
        metadata = pyos.guess_parameters(parser.filename)
    except GuessError:
        print "[-] Cannot guess video details. Please try manual mode"
        exit()

    title = metadata['title']
    season = metadata['season'] if 'season' in metadata else None
    episode = metadata['episode'] if 'episode' in metadata else None

    results = pyos.search_subtitle(title, season, episode)
    return results

def manualfetch(pyos, parser):
    try:
        title = parser.filename
        season = parser.season
        episode = parser.episode
    except AttributeError:
        pass

    results = pyos.search_subtitle(title, season, episode)
    return results


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
        results = manualfetch(pyos, parser)
    else:
        results = autofetch(pyos, parser)
    num_results = len(results['data'])

    if num_results == 0:
        print "[-] No subtitles found"
        return 1

    print "[+] Found %d subtitles" %(len(results['data']))
    print "[*] Downloading Subtitle.."
    idsubtitlefile = results['data'][0]['IDSubtitleFile']


    #Decide how to name the subtitle
    if parser.mode == 'manual':
        if parser.season is None or parser.episode is None:
            filename = "%s.srt" %(parser.filename)
        else:
            filename = "%s.S%02dE%02d.srt" %(parser.filename, parser.season, parser.episode)
            filename = filename.replace(" ", ".")
    else:
        filename = '.'.join(parser.filename.split(".")[:-1] + ['srt'])

    #Save the subtitle file
    pyos.download_subtitle(idsubtitlefile, filename)

    print "[+] Subtitles saved as %s" %(filename)

if __name__ == '__main__':
    main()
