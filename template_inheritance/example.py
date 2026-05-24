from flask import (
Flask,render_template, request,
url_for, redirect,
Response
)

app = Flask(__name__)

@app.route("/")
def home():
    pass


if __name__ == "__main__":
    app.run(debug=True)