__author__ = 'jmagady'

from app import yts_class, args_builder
import logging
from logging.handlers import RotatingFileHandler


yts_api = yts_class.Rawyts()  # initialize the yts_class
parg = args_builder.parser  # initialize the args parser
