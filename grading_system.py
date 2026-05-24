from flask import Flask ,render_template,request,redirect,url_for,session,Response

app = Flask(__name__)
app.secret_key = "myapp"

#Taking input from User
def data():
    name = str(input("Enter your name: "))
    math = float(input("Enter marks of Math: "))
    science = float(input("Enter marks of Science: "))
    english = float(input("Enter marks of English: "))


#home route
@app.route("/")
def home():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "12345":
        session['student'] = username

    else:
        return Response("Invalid credentials",mimetype="text/plain")

#Run flask server
if __name__ == "__main__":
    app.run(debug=True)