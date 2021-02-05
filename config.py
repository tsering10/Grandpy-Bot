# CONFIGURATION VARIABLES
import os 
import random, string
import logging

# see doc at http://flask.pocoo.org/docs/0.12/quickstart/ -> paragraph "SESSION"
SECRET_KEY = os.urandom(24)
# to get your JS API key go to https://developers.google.com/maps/documentation/javascript/get-api-key
GOOGLE_JS_KEY = "AIzaSyCijZFozLf948SNQzcGVkRaPZ-8wymgkkk"
# to get your GEO API key go to https://developers.google.com/maps/documentation/geocoding/get-api-key
GOOGLE_GEO_KEY = "AIzaSyC-DXpHl3cl41Gn6nAAF-FTF4NVJxZgSI4"


logging_config = dict(
    version=1,
    formatters={
        'simple': {'format': '%(levelname)s %(asctime)s { module name : %(module)s Line no : %(lineno)d} %(message)s'}
    },
    handlers={
        'h': {'class': 'logging.handlers.RotatingFileHandler',
              'filename': 'app/logly/logs/logger.log',
              'maxBytes': 1024 * 1024 * 5,
              'backupCount': 5,
              'level': 'DEBUG',
              'formatter': 'simple',
              'encoding': 'utf8'}
    },

    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)
