import json
from flask import Flask, render_template

app = Flask(__name__)

file = open("dicionario_translation_2.json", encoding='utf8')
db = json.load(file)

@app.route("/")
def home():
    return  render_template("home.html", title="Welcome!")

@app.route("/search")
def search():
    return  render_template("search.html")

@app.route("/terms")
def terms():
    return  render_template("terms.html", designations=db.keys(), excluded_terms = ["Palavra", "Significado"])

@app.route("/term/<t>")
def term(t):
    return  render_template("term.html", designation = t, value=db.get(t, "None"))

app.run(host="localhost", port=3000, debug=True)