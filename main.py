from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/hi")
def hi_there():
    return "<p>trolololol</p>"