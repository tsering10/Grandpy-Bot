import urllib.request
from typing import List
from urllib.error import HTTPError
import json
from app.starter import app
import logging
from typing import List, Set, Dict, Tuple, Optional

logger = logging.getLogger()


class MediaWiki:
    """
    This is a class to request connection to media wiki api and retrieve page id, geolocation and informtion
    based on query string

    """

    def __init__(self, latitude: float, longitude: float, query_key_string: List[str]):
        """
        The constructor for MediaWiki class

        Parameters: url_key_words --> list of string
        """
        self.latitude = latitude
        self.longitude = longitude
        self.query_key_string = "".join(query_key_string).replace(" ", "%20")
        self.page_id = 0
        self.data = {}
        self.wiki_result = ""

    def wiki_search(self):
        """ This method is to check media wiki api connection and retrieve its information in json"""
        base_url = "https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&srlimit=1&srsearch="
        search_url = base_url + f"{self.query_key_string}"
        try:
            content = urllib.request.urlopen(search_url)
            self.data = json.loads(content.read().decode("utf8"))

        except HTTPError as e:
            traceError = 'Mediawiki: search API request error: {}'.format(e)
            logger.error(traceError)
        except KeyError as error:
            # Output expected KeyErrors.
            logger.error(error)
        except IndexError as error:
            # Output expected IndexErrors.
            logger.error(error)
        except json.decoder.JSONDecodeError as error:
            # Output expected json decode errors.
            logger.error(error)

        if "search" in self.data['query'].keys():
            if len(self.data['query']['search']) > 0:
                self.page_id = self.data['query']['search'][0]['pageid']
        else:
            self.page_id = 0

    def geo_search(self):
        """ This method is used to make connection to media wik based on lat and lon and gets its page id"""

        mediawiki_url_coord = f"https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=1000&gslimit=1&format=json&gscoord={self.latitude}%7C{self.longitude}"
        try:
            content = urllib.request.urlopen(mediawiki_url_coord)
            self.data = json.loads(content.read().decode('utf-8'))
        except HTTPError as e:
            traceError = 'Mediawiki: geo search API request error : {}'.format(e)
            logger.error(traceError)
        except KeyError as error:
            # Output expected KeyErrors.
            logger.error(error)
        except IndexError as error:
            # Output expected IndexErrors.
            logger.error(error)
        except json.decoder.JSONDecodeError as error:
            # Output expected json decode errors.
            logger.error(error)

        if "geosearch" in self.data['query'].keys() and len(self.data['query']['geosearch']) > 0:
            self.page_id = self.data['query']['geosearch'][0]['pageid']
        else:
            self.page_id = 0

    #
    def wiki_page_finder(self) -> bool:
        """ function that finds the Wiki page by key words and coordinates """
        # by key words function
        self.wiki_search()
        # if the research by key words produces no results
        if self.page_id == 0:
            # research by coordinates function
            self.geo_search()
        else:
            # if the research by key words is good
            return True

        if self.page_id != 0:
            return True
        return False

    def get_extract(self) -> bool:
        """ This method is used to extract the information from media wiki api"""
        if self.wiki_page_finder():
            page_searching_url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=1&explaintext=1&exsentences=2&pageids={self.page_id}"
            try:
                content = urllib.request.urlopen(page_searching_url)
                self.data = json.loads(content.read().decode("utf8"))
                return True

            except HTTPError as e:
                traceError = "MediaWiki API error {} in page id finder".format(e)
                logger.error(traceError)
                return False
            except KeyError as error:
                # Output expected KeyErrors.
                logger.error(error)
                return False
            except IndexError as error:
                # Output expected IndexErrors.
                logger.error(error)
                return False
            except json.decoder.JSONDecodeError as error:
                # Output expected json decode errors.
                logger.error(error)
                return False

    def sentences_return(self) -> bool:
        """ Returns the two first sentences of Wiki page """
        # if content found
        if self.get_extract():
            if "query" in self.data.keys():
                self.wiki_result = self.data['query']['pages'][str(self.page_id)]['extract']
                return True
            return False
        # if content not found
        else:
            return False
