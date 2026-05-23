from flask import Flask,redirect,render_template,request,session,url_for,Response

#Create Flask Application
app = Flask(__name__)
app.secret_key = "specialKey"  #Must add secret key before using session


#Home route and using GET and POST methods
@app.route("/",methods=['GET','POST'])
def login():

    #Using POST method for sending information on Server
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "root" and password == "12345":
            session["userData"] = username #Store data in Session
            return redirect(url_for("next_page"))

        else:
            return Response("Incorrect username and password",mimetype="text/plain")

    #Returns HTML Simple Form
    return '''
    <form method = "POST">
    Username: <input type="text" name="username">
    Password: <input type="password" name="password">
    <input type="submit" value="Submit">
    </form>
   '''

#Next Page route
@app.route("/next_page")
def next_page():

    if "userData" in session:
        return f'''
        <h1>Thanks for filling the form</h1><br>
        <h3>Your data has been saved into Session</h3>
        <a href={url_for("logout")}> <p>Click here for logout</p></a>'''

    return redirect(url_for("login"))


#Login route
@app.route("/logout")
def logout():
    session.pop("userData",None)
    return redirect(url_for("login"))


#Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)