from flask import Flask

application = Flask(__name__)


@application.route("/")
def Hello():
    return "Hello world"
