from flask import render_template, request, redirect, url_for

from . import app

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #user = session.query(User).filter(User.username == username).first()
        #if user.password == password:
            # grant login
            #return redirect(url_for("ad_form"), code=302)
        

@app.route("/ad-form", methods=["GET", "POST"])
@require_login
def ad_form():
    if request.method == 'GET':
        our_user_id.
        # we call facebook api to get the data of the form | urllib
        #data = session.query(Facebook).filter(Facebook.user_id == our_user_id)
        
        return render_template("ad_form.html", form_data = data)
    elif request.method == 'POST':
        return redirect(url_for('home'), code=302)
        
