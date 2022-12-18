from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()
app.app_context()
if os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'ghci':
    print("Running in github mode")
    app.config.from_object('config.GithubCIConfig')

db = SQLAlchemy(app)


from api.models import Recipe

with app.app_context():
    db.create_all()
CORS(app)

from api import routes