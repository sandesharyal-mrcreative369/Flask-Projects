from flask import (Flask ,render_template,request,
                   session,Response,url_for,redirect,
                   )


app = Flask(__name__)
app.secret_key = "myapp"


#home route
@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        math = request.form.get("math")
        science = request.form.get("science")
        english = request.form.get("english")


        if username == "admin" and password == "12345":
            session['student'] = username
            return render_template(
                "submit.html",
                name=name,
                math=math,
                science=science,
                english=english
            )

        else:
            return Response("Invalid credentials",mimetype="text/plain")

    return render_template("home.html")


#Run flask server
if __name__ == "__main__":
    app.run(debug=True)