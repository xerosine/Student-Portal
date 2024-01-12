from flask import Flask, render_template, url_for, request, flash, current_app
import json, pymysql, os
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('LandingPage.html')

@app.route('/register')
def register():
    return render_template('FormPage.html')

@app.route('/allDetails')
def allDetails():
    return render_template('AllDetails.html')


if __name__ == "__main__":
    app.run(debug=True)