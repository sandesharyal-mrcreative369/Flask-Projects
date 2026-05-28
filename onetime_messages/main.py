from flask import (Flask,render_template,
                   request,redirect,url_for,session,
                   flash)

app = Flask(__name__)
session.secret_key = 'mySecretKey'

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        if not name:
            flash("Name not provided")
            return render_template('form.html')

        flash(f"Thank you {name} for your feedback messages")
        return redirect(url_for('thankyou'))

    return render_template('form.html')



if __name__=='__main__':
    app.run(debug=True)
