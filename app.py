from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/settings")
def settings():
    #pi-hole=dns
    #so it can communicate properly
    return render_template("settings.html")

if __name__=="__main__":
    app.run(debug=True)