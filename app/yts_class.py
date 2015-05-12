__author__ = 'jmagady'


from requests import get
from config import YTS_API_BASE, YTS_LIST_MOVIES_ENDPOINTS, YTS_LIST_UPCOMING


class Rawyts:
    """
    This is a python class wrapping the YTS v2 API. Most used methods are currently implemented
    """
    def __init__(self):
        pass

    def raw_upcoming(self):
        """
        This function pulls the upcoming movies list from yst

		Args:
		  None
		Returns:
		  Dictionary of values
		Raises:
		  No error checking is performed
		"""
        res = get(YTS_API_BASE + YTS_LIST_UPCOMING['json'])
        dic = res.json()
        return dic

    def raw_movie_list(self, limit=20, page=1, quality='ALL', rating=0, genre='ALL', sort='date_added', order='desc'):
        """
        This function will retrieve all movies that match the given parameters

		Args:
		    limit (int, optional): sets the limit on how many matches to return per page. int value between 1 - 50,
		    default is 20
		    page (int, optional): used to set the page number to see the next set of movies. eg: limit=15 and set=2
		    will show you movies 16-39
		    quality (str, optional): ability to select a quality type to filter by. valid options 720p, 1080p, 3D, ALL.
		    All is the default
		    rating (int, optional): set minimum movie rating for display. int between 0-9
		    genre (str, optional): display movies from chosen type genre. default is ALL. See www.imdb.com/genre/ for a
		    full list.
		    sort (str, optional): sorts results by the chosen method. Acceptable methods are: date, seeds, peers, size,
		    alphabet, rating, downloaded, year
		    order (str, optional): Orders the results with either ascending or descending,
		    acceptable methods are: desc, asc

		Returns:
		    returns a dictionary of dictionaries. The containing dictionary contains the keys "status", "status_message"
		    , and "data". "data" contains a dictionary with the following keys: "movie_count", "limit" (this is the
		    number of movies per page), "page_number" (the current page you are on), and "movies". "movies" contains the
		    actual movie data and contains the following keys: "id", "url", "imdb_code", "title", "title_long", "slug",
		    "year", "rating", "runtime", "genres" (This is a list for the value), "language", "mpa_rating",
		    "small_cover_image", "medium_cover_image", "state", "torrents". "torrents" contains a list of dictionaries
		    containing all the information for the actual torrents. The keys for each dictionary in the list are: "url",
		    "hash", "quality", "seeds", "peers", "size", "size_bytes", "date_uploaded", "date_uploaded_unix".

		    Page count is determined by dividing movie count by limit and adding 1 if the value is float #

		Raises:
		    currently no error checking is performed
		"""
        payload = {'limit': limit, 'page': page, 'quality': quality, 'minimum_rating': rating, 'genre': genre, 'sort_by': sort,
                   'order_by': order}
        res = get(YTS_API_BASE + YTS_LIST_MOVIES_ENDPOINTS['json'], params=payload)
        dic = res.json()
        # pagecount = dic['MovieCount']/limit
        # if isinstance(pagecount, float):
        # pagecount += 1

        return dic

    def raw_latest(self):
        """
        This pulls the last 20 movies that YTS has posted.

        Args:
            None

        Returns:
            returns a dictionary

        Raises:
            Currently no error checking is performed

        """
        res = get(YTS_API_BASE + YTS_LIST_MOVIES_ENDPOINTS['json'])
        dic = res.json()
        return dic

    def raw_movie_search(self, movie):
        payload = {'keywords': movie}
        res = get(YTS_API_BASE + YTS_LIST_MOVIES_ENDPOINTS['json'], params=payload)
        dic = res.json()
        return dic

    def raw_requests_page_count(self, limit=20):
        payload = {'limit': limit}
        res = get(YTS_API_BASE + YTS_LIST_MOVIES_ENDPOINTS['json'], params=payload)
        dic = res.json()
        pagecount = dic['data']['movie_count'] / limit
        if isinstance(pagecount, float):
            pagecount += 1

        return pagecount