#!/usr/bin/python2

from pyopensubtitles.pyopensubtitles import PyOpenSubtitles
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('show')
    parser.add_argument('season')
    parser.add_argument('episode')
    parser = parser.parse_args()

    pyos = PyOpenSubtitles()

    print "[*] Searching for subtitles.."
    results = pyos.search_subtitle(parser.show, parser.season, parser.episode)
    print "[+] Found %d subtitles" %(len(results))
    print "[*] Downloading Subtitle.."
    idsubtitlefile = results['data'][0]['IDSubtitleFile']
    filename = "%s.S%02dE%02d.srt" %(parser.show, int(parser.season), int(parser.episode))
    filename = filename.replace(" ", ".")

    pyos.download_subtitle(idsubtitlefile, filename)

    print "[+] Subtitles saved as %s" %(filename)

if __name__ == '__main__':
    main()
