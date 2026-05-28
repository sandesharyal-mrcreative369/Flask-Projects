from flask import Flask,render_template,request,session,url_for,redirect,flash
from registration_form import *

app = Flask(__name__)

@app.route("/")
def home():
    pass

if __name__=="__main__":
    app.run(debug=True)
