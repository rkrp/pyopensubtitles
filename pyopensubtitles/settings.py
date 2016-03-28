LANGUAGE = "eng"
USERAGENT = "OSTestUserAgent"

"""
Default credentials
If empty, logged in as guest
"""
USERNAME = ""
PASSWORD = ""

"""
URLs
"""
URLS = {
    'safe' : "https://api.opensubtitles.org/xml-rpc",
    'unsafe' : "http://api.opensubtitles.org/xml-rpc"
}

SAFETY_LEVEL = 'safe'



"""
DO NOT MODIFY ANYTHING BELOW THIS LINE
"""
URL = URLS[SAFETY_LEVEL]
