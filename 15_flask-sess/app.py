#Team MadCauseBad - Ryan Ma, Jessica Yeung, May Hathaway, William Li
#SoftDev
#K15 -- Sessions Greetings - Using cookies and creating login pages
#2020-12-10

from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
user = "dog"
passw = "cat"

@app.route("/", methods=['GET', 'POST'])
def loginpage():
    if(request.method == "POST"): # if there is an input, otherwise display the login page
        req = request.form
        session["username"] = req["username"] # stores cookies from forms
        session["passw"] = req["passw"]
        if(session["username"] != user and session["passw"] == passw): # error message assignment
            return render_template('login.html', error = "Wrong Username")
        elif(session["username"] == user and session["passw"] != passw):
            return render_template('login.html', error = "Wrong Password")
        elif(session["username"] != user and session["passw"] != passw):
            return render_template('login.html', error = "Wrong Username and Password")
        # if(session["username"] != user or session["passw"] != passw):
        #     return render_template('login.html', error = "Wrong Username or Password")
        # ^ if we were adhering to proper security practices
    if("username" in session and session["username"] == user and "passw" in session and session["passw"] == passw):
        return render_template( 'response.html', usern = session["username"])
    # checks if correct cookies exist and if so, display welcome page
    return render_template("login.html")

@app.route("/welcome", methods=['GET', 'POST'])
def logout():
    if(request.method == "POST"): # if the logout button has been pressed, otherwise keep displaying welcome page
        session.pop("username") # removes cookies upon logout
        session.pop("passw")
    if("username" in session and session["username"] == user and "passw" in session and session["passw"] == passw):
        return render_template("response.html", usern = session["username"])
    return render_template("login.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()