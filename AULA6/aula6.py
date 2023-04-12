from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"

@app.route("/search")
def search():
    return "<p>Hello, World!!!!</p>"

@app.route("/home")
def home_page():
    return  render_template("home.html", title="Welcome!")

@app.route("/termos")
def termos():
    return '''
    <h1 style='font-size:35px; text-align:center; font-family:arial; color:DarkRed;'>Dicionário Médico</h1>
    <p style='text-align:center; font-family:arial;'>Lista de termos</p>
    '''

@app.route("/creditos")
def creditos():
    return '''
    <h1 style='font-size:35px; text-align:center; font-family:arial; color:DarkRed;'>Dicionário Médico</h1>
    <p style='text-align:center; font-family:arial;'>Créditos</p>
    '''

app.run(host="localhost", port=3000, debug=True)