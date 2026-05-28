from flask import Flask,render_template,request,session,url_for,redirect,flash
from registration_form import *

app = Flask(__name__)
app.secret_key= "mySecretKey"

@app.route("/",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        email = form.email.data
        flash(f"Welcome {{name}}.Registration has been created!","successfully")
        return redirect(url_for("success"))

    return render_template("register.html",form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__=="__main__":
    app.run(debug=True)
