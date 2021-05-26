from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"]="bananas"

from app import routes