print('This is to build the Flash Card generator to prepare well for the topics')

# testing for the flask
from flask import Flask

print("is this app running")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

