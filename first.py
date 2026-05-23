#Importing Flask
from flask import Flask

#Creation of Flask Application
app = Flask(__name__)

#Create home route
@app.route("/")
def first():
    return "Hello Flask"


#Run Flask server
if __name__ == "__main__":
    app.run(debug=True)