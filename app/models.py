__author__ = 'jmagady'

import sqlalchemy as sa


db_engine = sa.create_engine('sqlite:///db.sqlite')
metadata = sa.MetaData()


# Table definition - yts_mapper_main
#
yts_mapper_main_table = sa.Table("yts_mapper_main", metadata,
    sa.Column('yts_movie_id', sa.Integer, sa.ForeignKey("yts_movie.id")),
    sa.Column('yts_quality_id', sa.Integer, sa.ForeignKey("yts_quality.id")),
    sa.Column('yts_torrent_hash_id', sa.Integer, sa.ForeignKey("yts_torrent_hash.id")))

# Table definition - yts_movie
#
yts_movie_table = sa.Table("yts_movie", metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('yts_years_id', sa.Integer, sa.ForeignKey("yts_years.id")),
    sa.Column('yts_library_state_id', sa.Integer, sa.ForeignKey("yts_library_status.id")),
    sa.Column('yts_map_rating_id', sa.Integer, sa.ForeignKey("yts_mpa_rating.id")),
    sa.Column('yts_rt_data', sa.Integer, sa.ForeignKey("yts_rt_data.id"), nullable=True),
    sa.Column('title', sa.String),
    sa.Column('title_long', sa.String),
    sa.Column('imdb_code', sa.String),
    sa.Column('runtime', sa.Integer),
    sa.Column('db_date_added', sa.Timestamp))

# Table definition - yts_genres
#
yts_genres_table = sa.Table("yts_genres", metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('genres', sa.String))

# Table definition - yts_quality
#
yts_quality_table = sa.Table("yts_quality", metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('quality', sa.String))

# Table definition - yts_years
#
yts_years_table = sa.Table("yts_years", metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('year', sa.Integer))

# Table definition - yts_mpa_rating
#
yts_mpa_rating_table = sa.Table("yts_mpa_rating", metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('rating', sa.String))

# Table definition - yts_torrent_hash
#
yts_torrent_hash_table = sa.Table("yts_torrent_hash", metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('yts_raw_files_id', sa.Integer, sa.ForeignKey("yts_raw_files.id"), nullable=True),
    sa.Column('hash', sa.String),
    sa.Column('size', sa.String),
    sa.Column('size_bytes', sa.Integer),
    sa.Column('seeds', sa.Integer),
    sa.Column('peers', sa.Integer),
    sa.Column('date_uploaded', sa.DateTime),
    sa.Column('db_t_date_added', sa.Timestamp))

# Table definition - yts_raw_files
#
yts_raw_files_table = sa.Table("yts_raw_files", metadata,
    sa.Column('id', sa.Integer, nullable=True, autoincrement=True, primary_key=True),
    sa.Column('tor_raw_files', sa.String),
    sa.Column('tor_raw_mfiles', sa.String),
    sa.Column('tor_raw_sfiles', sa.String, nullable=True))

# Table definition - yts_library_status
#
yts_library_status_table = sa.Table("yts_library_status", metadata,
    sa.Column('id', sa.Integer, nullable=True, autoincrement=True, primary_key=True),
    sa.Column('state', sa.String))

# Table definition - yts_lang
#
yts_lang_table = sa.Table("yts_lang", metadata,
    sa.Column('id', sa.Integer, nullable=True, autoincrement=True, primary_key=True),
    sa.Column('language', sa.Integer, nullable=True))

# Table definition - yts_genres_mapper
#
yts_genres_mapper_table = sa.Table("yts_genres_mapper", metadata,
    sa.Column('yts_movie_id', sa.Integer, sa.ForeignKey("yts_movie.id")),
    sa.Column('yts_genres_id', sa.Integer, sa.ForeignKey("yts_genres.id"), nullable=True))

# Table definition - yts_lang_mapper
#
yts_lang_mapper_table = sa.Table("yts_lang_mapper", metadata,
    sa.Column('yts_movie_id', sa.Integer, sa.ForeignKey("yts_movie.id")),
    sa.Column('yts_lang_id', sa.Integer, sa.ForeignKey("yts_lang.id")))

# Table definition - yts_rt_data
#
yts_rt_data_table = sa.Table("yts_rt_data", metadata,
    sa.Column('id', sa.Integer, nullable=True, autoincrement=True, primary_key=True),
    sa.Column('critics_score', sa.Numeric),
    sa.Column('critics_rating', sa.Numeric),
    sa.Column('audience_score', sa.Numeric))

# Table definition - yts_p_library
#
yts_p_library_table = sa.Table("yts_p_library", metadata,
    sa.Column('id', sa.Integer, nullable=True, autoincrement=True, primary_key=True),
    sa.Column('p_fname', sa.String),
    sa.Column('yts_movie_id', sa.Integer, sa.ForeignKey("yts_movie.id"), nullable=True),
    sa.Column('p_quality', sa.Integer, sa.ForeignKey("yts_quality.id")))


# Mapping Objects
class yts_mapper_main():
    def __init__(self, yts_movie_id, yts_quality_id, yts_torrent_hash_id):
        self.yts_movie_id = yts_movie_id
        self.yts_quality_id = yts_quality_id
        self.yts_torrent_hash_id = yts_torrent_hash_id

    def __repr__(self):
        return "<yts_mapper_main('%s', '%s', '%s')>" % (self.yts_movie_id, self.yts_quality_id, self.yts_torrent_hash_id)

class yts_movie():
    def __init__(self, id, yts_years_id, yts_library_state_id, yts_map_rating_id, yts_rt_data, title, title_long, imdb_code, runtime, db_date_added):
        self.id = id
        self.yts_years_id = yts_years_id
        self.yts_library_state_id = yts_library_state_id
        self.yts_map_rating_id = yts_map_rating_id
        self.yts_rt_data = yts_rt_data
        self.title = title
        self.title_long = title_long
        self.imdb_code = imdb_code
        self.runtime = runtime
        self.db_date_added = db_date_added

    def __repr__(self):
        return "<yts_movie('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.yts_years_id, self.yts_library_state_id, self.yts_map_rating_id, self.yts_rt_data, self.title, self.title_long, self.imdb_code, self.runtime, self.db_date_added)

class yts_genres():
    def __init__(self, id, genres):
        self.id = id
        self.genres = genres

    def __repr__(self):
        return "<yts_genres('%s', '%s')>" % (self.id, self.genres)

class yts_quality():
    def __init__(self, id, quality):
        self.id = id
        self.quality = quality

    def __repr__(self):
        return "<yts_quality('%s', '%s')>" % (self.id, self.quality)

class yts_years():
    def __init__(self, id, year):
        self.id = id
        self.year = year

    def __repr__(self):
        return "<yts_years('%s', '%s')>" % (self.id, self.year)

class yts_mpa_rating():
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

    def __repr__(self):
        return "<yts_mpa_rating('%s', '%s')>" % (self.id, self.rating)

class yts_torrent_hash():
    def __init__(self, id, yts_raw_files_id, hash, size, size_bytes, seeds, peers, date_uploaded, db_t_date_added):
        self.id = id
        self.yts_raw_files_id = yts_raw_files_id
        self.hash = hash
        self.size = size
        self.size_bytes = size_bytes
        self.seeds = seeds
        self.peers = peers
        self.date_uploaded = date_uploaded
        self.db_t_date_added = db_t_date_added

    def __repr__(self):
        return "<yts_torrent_hash('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.yts_raw_files_id, self.hash, self.size, self.size_bytes, self.seeds, self.peers, self.date_uploaded, self.db_t_date_added)

class yts_raw_files():
    def __init__(self, id, tor_raw_files, tor_raw_mfiles, tor_raw_sfiles):
        self.id = id
        self.tor_raw_files = tor_raw_files
        self.tor_raw_mfiles = tor_raw_mfiles
        self.tor_raw_sfiles = tor_raw_sfiles

    def __repr__(self):
        return "<yts_raw_files('%s', '%s', '%s', '%s')>" % (self.id, self.tor_raw_files, self.tor_raw_mfiles, self.tor_raw_sfiles)

class yts_library_status():
    def __init__(self, id, state):
        self.id = id
        self.state = state

    def __repr__(self):
        return "<yts_library_status('%s', '%s')>" % (self.id, self.state)

class yts_lang():
    def __init__(self, id, language):
        self.id = id
        self.language = language

    def __repr__(self):
        return "<yts_lang('%s', '%s')>" % (self.id, self.language)

class yts_genres_mapper():
    def __init__(self, yts_movie_id, yts_genres_id):
        self.yts_movie_id = yts_movie_id
        self.yts_genres_id = yts_genres_id

    def __repr__(self):
        return "<yts_genres_mapper('%s', '%s')>" % (self.yts_movie_id, self.yts_genres_id)

class yts_lang_mapper():
    def __init__(self, yts_movie_id, yts_lang_id):
        self.yts_movie_id = yts_movie_id
        self.yts_lang_id = yts_lang_id

    def __repr__(self):
        return "<yts_lang_mapper('%s', '%s')>" % (self.yts_movie_id, self.yts_lang_id)

class yts_rt_data():
    def __init__(self, id, critics_score, critics_rating, audience_score):
        self.id = id
        self.critics_score = critics_score
        self.critics_rating = critics_rating
        self.audience_score = audience_score

    def __repr__(self):
        return "<yts_rt_data('%s', '%s', '%s', '%s')>" % (self.id, self.critics_score, self.critics_rating, self.audience_score)

class yts_p_library():
    def __init__(self, id, p_fname, yts_movie_id, p_quality):
        self.id = id
        self.p_fname = p_fname
        self.yts_movie_id = yts_movie_id
        self.p_quality = p_quality

    def __repr__(self):
        return "<yts_p_library('%s', '%s', '%s', '%s')>" % (self.id, self.p_fname, self.yts_movie_id, self.p_quality)


# Declare mappings
mapper(yts_mapper_main, yts_mapper_main_table)
mapper(yts_movie, yts_movie_table)
mapper(yts_genres, yts_genres_table)
mapper(yts_quality, yts_quality_table)
mapper(yts_years, yts_years_table)
mapper(yts_mpa_rating, yts_mpa_rating_table)
mapper(yts_torrent_hash, yts_torrent_hash_table)
mapper(yts_raw_files, yts_raw_files_table)
mapper(yts_library_status, yts_library_status_table)
mapper(yts_lang, yts_lang_table)
mapper(yts_genres_mapper, yts_genres_mapper_table)
mapper(yts_lang_mapper, yts_lang_mapper_table)
mapper(yts_rt_data, yts_rt_data_table)
mapper(yts_p_library, yts_p_library_table)

# Create a session
session = sessionmaker(bind=db_engine)

