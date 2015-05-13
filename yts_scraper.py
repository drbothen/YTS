__author__ = 'jmagady'

from app import yts_api, parg, s
from app.models import YTS_MOVIE, YTS_YEAR, YTS_MPA_RATING, YTS_LIBRARY_STATUS, YTS_GENRES, YTS_LANG, YTS_QUALITY, YTS_TORRENT_HASH
import sys

def main():
    """
    if len(sys.argv) is 1:  # checks to see if any flags are present. if not display help sys.argv will always be atleats 1.
        parg.print_help()  # displays help
        sys.exit()  # exits the system

    rargs = parg.parse_args(sys.argv[1:])  # parse the args.

    rargs.update
    """
#ytsData = yts_api.raw_movie_list()
pagecount = yts_api.raw_requests_page_count()

for page in range(1, pagecount + 1):
    ytsData = yts_api.raw_movie_list(page=page)
    print('currently on page {page} of {pages}'.format(page=page,pages=pagecount))

    for movie in ytsData['data']['movies']:
        mentry = YTS_MOVIE(title=movie['title'],
                           title_long=movie['title_long'],
                           imdb_code=movie['imdb_code'],
                           runtime=movie['runtime'])
        mentry.year = YTS_YEAR.get(s, movie['year'])
        mentry.mpa_rating = YTS_MPA_RATING.get(s, movie['mpa_rating'])
        mentry.state = YTS_LIBRARY_STATUS.get(s, movie['state'])
        mentry.lang = YTS_LANG.get(s, movie['language'])
        lgenre = []
        for genre in movie['genres']:
            lgenre.append(YTS_GENRES.get(s, genre))
        mentry.genres = lgenre

        print("The movie: {Movie} has {tnum} torrents".format(Movie=movie['title'], tnum=len(movie['torrents'])))
        s.add(mentry)
        s.commit()



if __name__ == '__main__':
    main()