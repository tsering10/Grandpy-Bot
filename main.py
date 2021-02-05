#! /usr/bin/env python

# to launch the server from console: "python main.py"
from app import app
from config import logging_config

from logging.config import dictConfig
# from app.logly.logging_config
dictConfig(logging_config)

if __name__ == '__main__':
    app.run(debug=True)
