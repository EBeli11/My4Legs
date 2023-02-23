import os
from flask import Flask, render_template, g
from utils.languages import LANGUAGES
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = os.urandom(24)

toolbar = DebugToolbarExtension(app)

@app.before_request
def before_request():
    g.language = 'en'

@app.route("/")
def index():
    return render_template("index.html", lang=LANGUAGES[g.language])

@app.route("/about")
def about():
    return render_template("about.html", lang=LANGUAGES[g.language])

@app.route("/service")
def service():
    return render_template("service.html", lang=LANGUAGES[g.language])

@app.route('/price')
def price():
    return render_template('price.html', lang=LANGUAGES[g.language])

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
