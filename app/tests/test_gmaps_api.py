from ..utils.googlemaps_api import GoogleApi  # import of test's target class
import urllib.request  # import urllib for request/response simulation
from io import BytesIO  # to create an object where it will be possible call the read() method
import json


class TestGoogleApi:
    """ Test class for google map api  """

    def setup_method(self):
        """ setup_method function called during the TestGoogleApi class test """
        self.address = "7 Cité Paradis, 75010 Paris, France"
        self.google_Api_Object = GoogleApi(self.address)

    def test_instance(self):
        """Test success if the data returned is a valid instance of GoogleApi object"""
        assert (isinstance(self.google_Api_Object, GoogleApi))

    def test_geocode(self, monkeypatch):
        """ geocoding service test with monkeypatch helper:
            Googlemaps API is simulated, a response in json format is expected
            Mocks http request via urllib.request module
        """

        # open in read mode the json file with gmaps API data
        with open("geo_data.json", "r", encoding="utf8") as f:
            results = json.load(f)

        # BytesIO class utilisation
        self.results = BytesIO(json.dumps(results).encode())

        def mock_return(request):
            return self.results

        # monkeypatch.setattr() method to change the returned value
        monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

        # expected returned values
        assert self.google_Api_Object.gmap_address(self.google_Api_Object.query_key_string) is True
        assert (type(self.google_Api_Object.latitude) is float)
        assert self.google_Api_Object.latitude == 48.8747265
        assert self.google_Api_Object.longitude == 2.3505517
