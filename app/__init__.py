__author__ = 'jmagady'

from app import yts_class, args_builder
from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from logging.handlers import RotatingFileHandler


yts_api = yts_class.Rawyts()  # initialize the yts_class
parg = args_builder.parser  # initialize the args parser
engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()
