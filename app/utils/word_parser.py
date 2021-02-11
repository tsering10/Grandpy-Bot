from unidecode import unidecode
import re
import json
import os
from typing import List, Set, Dict, Tuple, Optional


class WordParser:
    """ This class is used to cut the sentence into words that you will then analyze to keep only the keywords"""

    def __init__(self, query:str):
        """
        The constructor for WordParser class

        Parameters: query --> string
        """
        self.query = unidecode(query)
        path = os.path.abspath(os.path.dirname(__file__)) + "/stop_words_fr.json"
        # load french stop words
        with open(path, "r", encoding="utf-8") as f:
            self.stop_words = json.load(f)['stop_words']
        self.query_keywords_list = self.pre_process()
        self.query_keys = self.parser(self.query_keywords_list)
        self.query_key_string = self.key_word_string(self.query_keys)

    def pre_process(self):
        # remove special characters and digits
        query = re.sub("(\\d|\\W)+", " ", self.query.lower()).strip()
        return list(query.split(" "))

    def parser(self, query_keywords_list: List[str]):
        # get keywords
        return [w for w in self.query_keywords_list if w not in self.stop_words]

    def key_word_string(self, query_keys: List[str]):
        # get keyword in string
        return ','.join(self.query_keys)
