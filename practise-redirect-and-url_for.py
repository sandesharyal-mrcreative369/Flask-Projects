#Importing Flask
from flask import Flask, url_for,redirect


#Creation of Flask object
app = Flask(__name__)


#Home route
@app.route("/")
def home():
    return redirect(url_for("page"))

#Welcome page route
@app.route("/welcome")
def welcome():
    return "<h1>Hello This is my flask first program</h1>"

#Next Page route
@app.route("/next-page")
def page():
    return '''
    <h3>Click here for next page</h3>
    <a href="welcome">Go to next page<a/>
    '''

#Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)