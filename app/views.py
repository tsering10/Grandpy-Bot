# -*-coding:utf-8-*-
from flask import render_template, request
from flask import jsonify
from app.utils import word_parser, googlemaps_api, mediawiki_api
from .starter import app
from .utils.answer_strings import AnswerString


@app.route('/')
@app.route('/index/')
def index():
    """Main page of the web app"""
    # GOOGLE_JS_KEY to load google map
    return render_template('index.html', gmap_api_key=app.config['GOOGLE_GEO_KEY'])


@app.route('/results/', methods=['GET', 'POST'])
def results():
    # Get the query
    query = request.args.get('query')
    # parse the query to keep the keywords (an address)
    query_parser = word_parser.WordParser(query)

    # create an object to call the google map geocoding API
    google_api_object = googlemaps_api.GoogleApi(query_parser.query_key_string)
    # create an object to get all the answer strings
    if google_api_object.gmap_address(google_api_object.query_key_string) is True:
        address_value = google_api_object.address
        longitude = google_api_object.longitude
        latitude = google_api_object.latitude
        # create an object to call Mediawiki api
        wiki_api_object = mediawiki_api.MediaWiki(latitude, longitude, query_parser.query_key_string)
        if wiki_api_object.sentences_return() is True:
            wiki_result = wiki_api_object.wiki_result
            wiki_id = wiki_api_object.page_id
            # create a json response object if the response it ok
            response = {"response": {"Gp_answer_gmap": AnswerString.geo_answer_string.value,
                                     "Gp_answer_wiki": AnswerString.wiki_answer_string.value,
                                     "gmap": address_value, "wiki": wiki_result, "wiki_id": wiki_id,
                                     "latitude": latitude, "longitude": longitude}}
            return jsonify(response)

        else:
            # create a json response object if  no response from mediawiki
            response = {"response": {"Gp_answer_gmap": AnswerString.geo_answer_string.value,
                                     "Gp_answer_wiki": AnswerString.wiki_no_response_answer_string.value,
                                     "gmap": address_value,
                                     "wiki": "ZERO_RESULT", "latitude": latitude,
                                     "longitude": longitude}}
            return jsonify(response)

    else:
        # No response
        response = {"response": {"gmap": "NO_RESULT", "wiki": "NO_RESULT",
                                 "Gp_answer": AnswerString.geo_no_response_answer_string.value}}
        return jsonify(response)
