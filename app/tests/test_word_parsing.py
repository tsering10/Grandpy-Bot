from ..utils.word_parser import WordParser


class TestParser:
    def setup_method(self):
        query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms"
        self.parser = WordParser(query)

    def test_parsing(self):
        assert type(self.parser.query_keywords_list) is list
        assert self.parser.query_keys == ['openclassrooms']
        assert self.parser.query_key_string == 'openclassrooms'
