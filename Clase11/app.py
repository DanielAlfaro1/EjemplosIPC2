from flask import Flask
from routes.rutas import ejemplo

app = Flask(__name__)
app.register_blueprint(ejemplo)
