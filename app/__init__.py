from flask import Flask
from flask_cors import CORS
import logging
import sys

app = Flask(__name__)
cors = CORS(app, resources={r"/get-campaign-info": {"origins": "*"}})
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

from . import land
