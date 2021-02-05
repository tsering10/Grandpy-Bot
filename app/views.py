# -*-coding:utf-8-*-
import json

from flask import render_template, request
from flask import jsonify
from app.utils import word_parser, googlemaps_api, mediawiki_api  # , answer_strings

from .starter import app
from .utils.answer_strings import AnswerString


@app.route('/')
@app.route('/index/')
def index():
    """Main page of the web app"""
    # GOOGLE_JS_KEY to load google map
    return render_template('index.html', gmap_api_key=app.config['GOOGLE_JS_KEY'])

#
@app.route('/results/', methods=['GET','POST'])
def results():
    # Get the query
    query = request.args.get('query')
    # parse the query to keep the keywords (an address)
    query_parser = word_parser.WordParser(query)

    # create an object to call the google map geocoding API
    google_Api_Object = googlemaps_api.GoogleApi(query_parser.query_key_string)
    # create an object to get all the answer strings
    if google_Api_Object.gmap_address(google_Api_Object.query_key_string) is True:
        address_value = google_Api_Object.address
        longitude = google_Api_Object.longitude
        latitude = google_Api_Object.latitude
        # create an object to call Mediawiki api
        wiki_Api_Object = mediawiki_api.MediaWiki(latitude, longitude, query_parser.query_key_string)
        if wiki_Api_Object.sentences_return() is True:
            wiki_result = wiki_Api_Object.wiki_result
            wiki_id = wiki_Api_Object.page_id
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
        # no response
        response = {"response": {"gmap": "NO_RESULT", "wiki": "NO_RESULT",
                                 "Gp_answer": AnswerString.geo_no_response_answer_string.value}}
        return jsonify(response)
