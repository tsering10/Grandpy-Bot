from flask import Flask
from flask_cors import CORS

# Cross Origin Ressource Sharing
# see (doc. at https://pypi.python.org/pypi/Flask-Cors)

app = Flask(__name__)
#Cross Origin Ressource Sharing Allowing
CORS(app)
app.config.from_object('config')