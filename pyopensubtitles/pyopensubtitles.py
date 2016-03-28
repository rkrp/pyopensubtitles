import xmlrpclib
import zlib
from settings import *

class PyOpenSubtitles:
    def __init__(self):
        self.remote = xmlrpclib.ServerProxy(URL)
        session = self.remote.LogIn(USERNAME, PASSWORD, LANGUAGE, USERAGENT)
        if session['status'] != "200 OK":
            raise LoginError

        self.token = session['token']

    def search_subtitle(self, query, season, episode):
        payload = {
                'query' : query,
                'season' : season,
                'episode': episode,
                'sublanguageid' : LANGUAGE,
        }

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

class LoginError:
    def __init__(self):
        self.value = value
    def __str__(self):
        return repr(self.value)

