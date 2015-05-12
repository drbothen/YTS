__author__ = 'jmagady'

from app import yts_api, parg, s
from app.models import YTS_MOVIE, YTS_YEAR, YTS_MPA_RATING
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
        s.add(mentry)
        s.commit()



if __name__ == '__main__':
    main()