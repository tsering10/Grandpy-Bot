from ..utils.mediawiki_api import MediaWiki
import urllib.request  
from .. import app
from io import BytesIO  
import json


class TestMediaWiki:
    """ class to test media wiki api"""
    def setup_method(self):
        """ setup_method function called during the TestMediaWiki class test """
        self.wiki_Api_Object = MediaWiki(48.8747578, 2.350564700000001, ['openclassrooms'])
        with open("data_wiki.json", "r", encoding="utf8") as mockfile:
            self.mediawiki_extracts_mock_data = json.load(mockfile)
    
    def test_instance(self):
        """Test success if the  returned  object is a valid instance of GoogleApi object"""
        assert (isinstance(self.wiki_Api_Object, MediaWiki))

    def test_search(self):
        """ Test success if the return page id is an expected page id"""
        self.wiki_Api_Object.wiki_search()
        assert self.wiki_Api_Object.page_id == 4338589


    def test_get_extracts(self, monkeypatch):
        """
        :Test success conditions:
        The Extracts API returns a JSON result fitting expectations.
        Mocks http request via urllib.request module
        IMPORTANT : random_place must be set to 0 in the instanciation ↑
        """
        def mockreturn(url):
            return BytesIO(json.dumps(self.mediawiki_extracts_mock_data).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        self.wiki_Api_Object.sentences_return()

        assert self.mediawiki_extracts_mock_data == self.wiki_Api_Object.data
