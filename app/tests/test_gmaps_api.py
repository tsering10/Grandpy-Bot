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
        with open(
            "geo_data.json", "r", encoding="utf8"
        ) as mockfile:
            self.gmaps_mock_data = json.load(mockfile)

        self.address_lat = 48.8747265
        self.address_lng = 2.3505517

    def test_instance(self):
        """Test success if the data returned is a valid instance of GoogleApi object"""
        assert (isinstance(self.google_Api_Object, GoogleApi))

    
    def test_geocode(self, monkeypatch):
        """ geocoding service test with monkeypatch helper:
            Googlemaps API is simulated, a response in json format is expected
            Mocks http request via urllib.request module
        """
        def mockreturn(url):
            return BytesIO(json.dumps(self.gmaps_mock_data).encode())

        # monkeypatch.setattr() method to change the returned value
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        # expected returned values
        assert self.google_Api_Object.gmap_address(self.google_Api_Object.query_key_string) is True
        
    def test_lat_lng_values(self):
        assert(type(self.address_lat) is float)
        assert(type(self.address_lng) is float)
        assert(self.address_lat == self.gmaps_mock_data["results"][0][
            "geometry"]["location"]["lat"])
        
        assert(self.address_lng == self.gmaps_mock_data["results"][0][
            "geometry"]["location"]["lng"])
        
        
    
