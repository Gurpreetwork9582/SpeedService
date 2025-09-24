from flask import  render_template,url_for,request, redirect,flash
from SpeedService.models import User
from SpeedService import app,db





@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# render_temp is a function which needs to be imported
# home.html is the file that you create seperatly in which all the web dev code is there


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        location = request.form.get("location")

        # Save to DB
        new_user = User(name=name, email=email, location=location)
        db.session.add(new_user)
        db.session.commit()
        flash("form submitted Successfully, We will be in touch!","success")
        return redirect(url_for('about'))
    return render_template("about.html")

@app.route("/Returnpage")
def success():
    return  render_template("Returnpage.html")

@app.route("/login")
def login():
    return render_template("login.html")

