from flask import Flask, render_template

app = Flask(__name__)

Post = [{"Name": "Gurpreet Singh", "Test": "Hello"}, {"Name": "Kunal"}]

title1 = "HOME - title"
title2 = "ABOUT - title"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=Post, titles=title1)


# render_temp is a function which needs to be imported
# home.html is the file that you create seperatly in which all the web dev code is there


@app.route("/about")
def about():
    return render_template("about.html", titles=title2)


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
