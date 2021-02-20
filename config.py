import os 
import logging

# see doc at http://flask.pocoo.org/docs/0.12/quickstart/ -> paragraph "SESSION"
SECRET_KEY = os.urandom(24)
# to get your JS API key go to https://developers.google.com/maps/documentation/javascript/get-api-key
# to get your GEO API key go to https://developers.google.com/maps/documentation/geocoding/get-api-key
GOOGLE_GEO_KEY = os.environ.get('GOOGLE_GEO_KEY')

# config for logging
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
