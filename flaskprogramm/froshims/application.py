from flask import Flask, redirect, render_template, request, sessions, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form["Name"] == "" or request.form["Dorm"] == "":
        return render_template("failure.html")
    return render_template('success.html')
