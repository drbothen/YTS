__author__ = 'jmagady'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


Base = declarative_base()

#  Association Table
yts_genres_mapper = Table(
    "yts_genres_mapper",
    Base.metadata,
    Column("yts_movie_id", Integer, ForeignKey("yts_movie.id")),
    Column("yts_genres_id", Integer, ForeignKey("yts_genres.id"))
)

#  Association Table
yts_mapper_main = Table(
    "yts_mapper_main",
    Base.metadata,
    Column("yts_movie_id", Integer, ForeignKey("yts_movie.id")),
    Column("yts_quality_id", Integer, ForeignKey("yts_quality.id")),
    Column("yts_torrent_hash_id", Integer, ForeignKey("yts_torrent_hash.id"))
)

class YTS_MOVIE(Base):
    __tablename__ = 'yts_movie'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    yts_year_id = Column(Integer, ForeignKey('yts_year.id'))  # creates a foreignKey for a 1 to many relation ship (This is the many side)
    yts_mpa_rating_id = Column(Integer, ForeignKey('yts_mpa_rating.id'))
    yts_library_status_id = Column(Integer, ForeignKey('yts_library_status.id'))
    yts_lang_id = Column(Integer, ForeignKey('yts_lang.id'))
    title = Column(String(64), index=True, nullable=False)
    title_long = Column(String(64), nullable=False)
    imdb_code = Column(String(64), nullable=False)
    runtime = Column(Integer, nullable=False)
    db_date_added = Column(DateTime, nullable=False, default=func.now())

    genres = relationship('YTS_GENRES',
                          backref='movies',
                          secondary=yts_genres_mapper)
    torrent = relationship('YTS_TORRENT_HASH',
                           backref='movies',
                           secondary=yts_mapper_main)
    quality = relationship('YTS_QUALITY',
                           backref='movies',
                           secondary=yts_mapper_main)

    def __repr__(self):
        return '<YTS_MOVIES {name}>'.format(name=self.name)


class YTS_YEAR(Base):
    __tablename__ = 'yts_year'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    year = Column(Integer, nullable=False)
    movie = relationship("YTS_MOVIE", backref="year")

    @staticmethod  # Checks to see if entry is already in Database
    def get(dbsession, year):
        obj = dbsession.query(YTS_YEAR).filter(YTS_YEAR.year == year).first()
        if not obj:
            obj = YTS_YEAR(year=year)
        return obj

class YTS_MPA_RATING(Base):
    __tablename__ = 'yts_mpa_rating'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    rating = Column(String(10), nullable=False)
    movie = relationship("YTS_MOVIE",
                         backref="mpa_rating")

    @staticmethod # Checks to see if entry is already in Database
    def get(dbsession, rating):
        obj = dbsession.query(YTS_MPA_RATING).filter(YTS_MPA_RATING.rating == rating).first()
        if not obj:
            obj = YTS_MPA_RATING(rating=rating)
        return obj

class YTS_LIBRARY_STATUS(Base):
    __tablename__ = 'yts_library_status'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    state = Column(String(50), nullable=False)
    movie = relationship("YTS_MOVIE",
                         backref="state")

    @staticmethod  # Checks to see if entry is already in Database
    def get(dbsession, state):
        obj = dbsession.query(YTS_LIBRARY_STATUS).filter(YTS_LIBRARY_STATUS.state == state).first()
        if not obj:
            obj = YTS_LIBRARY_STATUS(state=state)
        return obj

class YTS_GENRES(Base):
    __tablename__ = 'yts_genres'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    genres = Column(String(50), nullable=False)

    @staticmethod  # Checks to see if entry is already in Database
    def get(dbsession, genres):
        obj = dbsession.query(YTS_GENRES).filter(YTS_GENRES.genres == genres).first()
        if not obj:
            obj = YTS_GENRES(genres=genres)
        return obj

class YTS_LANG(Base):
    __tablename__ = 'yts_lang'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    language = Column(String(50), nullable=False)
    movie = relationship("YTS_MOVIE",
                         backref="lang")

    @staticmethod  # Checks to see if entry is already in Database
    def get(dbsession, language):
        obj = dbsession.query(YTS_LANG).filter(YTS_LANG.language == language).first()
        if not obj:
            obj = YTS_LANG(language=language)
        return obj

class YTS_TORRENT_HASH(Base):
    __tablename__ = 'yts_torrent_hash'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    hash = Column(String(512), nullable=False)
    size = Column(String(20), nullable=False)
    size_bytes = Column(Integer, nullable=False)
    date_uploaded = Column(DateTime, nullable=False)
    db_t_date_added = Column(DateTime, nullable=False, default=func.now())

    @staticmethod  # Checks to see if entry is already in Database
    def get(dbsession, hash, size, size_bytes, date_uploaded):
        obj = dbsession.query(YTS_TORRENT_HASH).filter(YTS_TORRENT_HASH.hash == hash).first()
        if not obj:
            obj = YTS_LANG(hash=YTS_TORRENT_HASH, size=size, size_bytes=size_bytes, date_uploaded=date_uploaded)
        return obj

class YTS_QUALITY(Base):
    __tablename__ = 'yts_quality'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    quality = Column(String(20), nullable=False)

    @staticmethod  # Checks to see if entry is already in Database
    def get(dbsession, quality):
        obj = dbsession.query(YTS_QUALITY).filter(YTS_QUALITY.quality == quality).first()
        if not obj:
            obj = YTS_QUALITY(quality=quality)
        return obj