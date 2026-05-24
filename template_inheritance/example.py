#Imported Libraries
from flask import (
Flask,render_template
)

#Create and Flask application
app = Flask(__name__)

#Home route
@app.route("/")
def home():
    return render_template("home.html")

#about route
@app.route("/about")
def about():
    return render_template("about.html")

#welcome route
@app.route("/welcome")
def contact():
    return render_template("welcome.html")


#Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)