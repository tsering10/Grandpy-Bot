from enum import Enum


class AnswerString(Enum):
    geo_answer_string = "Votre adresse :"
    wiki_answer_string = "Informations sur ce lieu :"
    geo_no_response_answer_string = "Pouvez-vous répéter votre question ...... svp"
    wiki_no_response_answer_string = "Désolé pas d'informations disponibles"
