from ..utils.mediawiki_api import MediaWiki
import urllib.request  # import urllib for request/response simulation
from .. import app
from io import BytesIO  # to create an object where it will be possible call the read() method
import json


class TestMediaWiki:
    """ class to test media wiki api"""
    def setup_method(self):
        """ setup_method function called during the TestMediaWiki class test """
        self.wiki_Api_Object = MediaWiki(48.8747578, 2.350564700000001, ['openclassrooms'])

    def test_instance(self):
        """Test success if the  returned  object is a valid instance of GoogleApi object"""
        assert (isinstance(self.wiki_Api_Object, MediaWiki))

    def test_search(self):
        """ Test success if the return page id is an expected page id"""
        self.wiki_Api_Object.wiki_search()
        assert self.wiki_Api_Object.page_id == 4338589

    def test_geo(self, monkeypatch):
        with open("mediawiki_api_data.json", "r") as f:
            self.returned_data = json.load(f)
            self.returned_dumps = json.dumps(self.returned_data)

        def mock_return(request):
            return BytesIO(self.returned_dumps.encode())

        # monkeypatch.setattr() method to change the returned value
        monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

        # expected returned values
        assert self.wiki_Api_Object.sentences_return() is True
        # assert self.wiki_Api_Object.page_id == 4338589
