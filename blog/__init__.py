from flask import Flask

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

from . import views
from . import models
# Connect sqlalchemy to app
models.db.init_app(app)