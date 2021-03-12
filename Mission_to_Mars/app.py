from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# import scrape mars py file 


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    return "Hello World"

@app.route("/scrape")
def scrape():
   
    return "Scrape is working"


if __name__ == "__main__":
    app.run(debug=True)