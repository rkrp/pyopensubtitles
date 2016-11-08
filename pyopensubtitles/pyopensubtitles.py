from guessit import guessit
import xmlrpclib
import zlib
from settings import *
from exceptions import *

class PyOpenSubtitles:
    def __init__(self):
        self.remote = xmlrpclib.ServerProxy(URL)
        session = self.remote.LogIn(USERNAME, PASSWORD, LANGUAGE, USERAGENT)
        if session['status'] != "200 OK":
            raise LoginError(session['status'])

        self.token = session['token']

    def guess_parameters(self, filename):
        params = guessit(filename)
        retval = dict()
        try:
            retval['title'] = params['title']
        except KeyError:
            raise GuessError("Cannot guess title")

        try:
            retval['season'] = params['season']
            retval['episode'] = params['episode']
        except KeyError:
            pass

        return retval

    def search_subtitle(self, query, season=None, episode=None):

        payload = {
                'query' : query,
                'sublanguageid' : LANGUAGE,
        }

        if season != None:
            payload['season'] = season

            if episode != None:
                payload['episode'] = episode


        option = {
                'limit' : 10
        }

        results = self.remote.SearchSubtitles(self.token, [payload], option)
        return results

    def download_subtitle(self, idsubtitlefile, filename):
        response = self.remote.DownloadSubtitles(self.token, [idsubtitlefile])
        compressed = response['data'][0]['data'].decode('base64')
        data = zlib.decompress(compressed, 16 + zlib.MAX_WBITS)
        with open(filename, 'w') as fp:
            fp.write(data)

    def makecall(self):
        pass
