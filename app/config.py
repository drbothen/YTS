__author__ = 'jmagady'
#from app import lt
import tempfile

# misc config
tempdir = tempfile.mkdtemp(prefix="yts.")

# YTS URI Configuration
YTS_API_BASE = "https://yts.to/api/v2/"
YTS_LIST_MOVIES_ENDPOINTS = {
    'json': 'list_movies.json',
    'jsonp': 'list_movies.jsonp',
    'xml': 'list_movies.xml'
}
YTS_MOVIE_DETAILS_ENDPOINTS = {
    'json': 'movie_details.json',
    'jsonp': 'movie_details.jsonp',
    'xml': 'movie_details.xml'
}
YTS_MOVIE_SUGGESTIONS_ENDPOINTS = {
    'json': 'movie_suggestions.json',
    'jsonp': 'movie_suggestions.jsonp',
    'xml': 'movie_suggestions.xml'
}
YTS_MOVIE_COMMENTS_ENDPOINTS = {
    'json': 'movie_comments.json',
    'jsonp': 'movie_comments.jsonp',
    'xml': 'movie_comments.xml'
}
YTS_MOVIE_REVIEWS_ENDPOINTS = {
    'json': 'movie_reviews.json',
    'jsonp': 'movie_reviews.jsonp',
    'xml': 'movie_reviews.xml'
}
YTS_PARENTAL_GUIDES_ENDPOINTS = {
    'json': 'movie_parental_guides.json',
    'jsonp': 'movie_parental_guides.jsonp',
    'xml': 'movie_parental_guides.xml'
}
YTS_LIST_UPCOMING = {
    'json': 'list_upcoming.json',
    'jsonp': 'list_upcoming.jsonp',
    'xml': 'list_upcoming.xml'
}

# Thread Workers
YTS_WEB_T_WORKERS = 10

# Args Builder
YTS_DESC_ARGS = "This program ties into YTS api and builds a database. \
It can also send magnetlinks to transmission for downloading"

# libtorrent config (experimental)
#params = {
#    'trackers': ['http://exodus.desync.com:6969/announce',
#                 'udp://tracker.openbittorrent.com:80/announce',
#                 'udp://open.demonii.com:1337/announce',
#                 'udp://exodus.desync.com:6969/announce',
#                 'udp://tracker.yify-torrents.com/announce'],
#    'save_path': tempdir,
#    'duplicate_is_error': True,
#    'storage_mode': lt.storage_mode_t(2),
#   'paused': False,
#    'auto_managed': True,
#    'duplicate_is_error': True
#}

# magnet creation params
trackers = ['udp://open.demonii.com:1337',
            'udp://tracker.istole.it:80',
            'http://tracker.yify-torrents.com/announce',
            'udp://tracker.publicbt.com:80',
            'udp://tracker.openbittorrent.com:80',
            'udp://tracker.coppersurfer.tk:6969',
            'udp://exodus.desync.com:6969',
            'http://exodus.desync.com:6969/announce']
