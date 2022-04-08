from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    if method.request == "POST":
        return "<p>Hello, World!</p>"
    else:
         return "<p>Hello, World!</p>"