import urllib.request
from app.starter import app
from urllib.error import HTTPError
import json
import logging
from json.decoder import JSONDecodeError

logger = logging.getLogger()


class GoogleApi:
    """
        This is a class for checking google map api request and get lat, lon and address
    """

    def __init__(self, url_key_words: str):
        """
        The constructor for GoogleApi class

        Parameters: url_key_words: string
        """
        self.key = app.config['GOOGLE_GEO_KEY']
        self.query_key_string = url_key_words
        self.address = ""
        self.longitude = 0
        self.latitude = 0
        self.data = {}

    def gmap_response(self) -> bool:
        """ Returns True or False if the request to google map is success or not"""
        if self.key is not None:
            endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?address={self.query_key_string}&key={self.key}"
        try:
            # Ping google map for the result
            webURL = urllib.request.urlopen(endpoint)
            content = webURL.read()
            self.data = json.loads(content.decode('utf-8'))
            return True

        except (HTTPError, KeyError, IndexError, JSONDecodeError) as error:
            # Output expected error
            logger.error(error)
            return False

    def gmap_address(self, query_keywords: str) -> bool:
        """ returns true if the request is good and then get the respective values else false"""
        if self.gmap_response():
            if 'status' in self.data.keys() and self.data['status'] == "OK":
                self.address = self.data['results'][0]['formatted_address']
                self.longitude = self.data['results'][0]['geometry']['location']['lng']
                self.latitude = self.data['results'][0]['geometry']['location']['lat']
                return True
            else:
                return False
        return False
