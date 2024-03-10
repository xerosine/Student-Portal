from flask import Flask, render_template, url_for, request, flash, current_app
import json, pymysql, os
from flaskext.mysql import MySQL

app = Flask(__name__)

# timeout = 10
# connection = pymysql.connect(
#   charset="utf8mb4",
#   connect_timeout=timeout,
#   cursorclass=pymysql.cursors.DictCursor,
#   db="defaultdb",
#   host="mysql-1642f47c-ayangaoluwamurewa-8ec6.a.aivencloud.com",
#   password="AVNS_b4us0vHkXgy29lgGlq2",
#   read_timeout=timeout,
#   port=10343,
#   user="avnadmin",
#   write_timeout=timeout,
# )

@app.route('/')
def landing():
    return render_template('LandingPage.html')

@app.route('/register')
def register():
    return render_template('FormPage.html')

@app.route('/details')
def details():
    return render_template('AllDetails.html')

@app.route('/profile')
def profile():
    return render_template('profilePage.html')


if __name__ == "__main__":
    app.run(debug=True)