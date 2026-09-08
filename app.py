from flask import Flask, render_template, redirect, url_for
import pihole
app = Flask(__name__)

@app.route("/")
def home():
    stats = pihole.call()
    return render_template("home.html",
                           queries_today =stats[0],
                           queries_blocked = stats[1],
                           percent_blocked=stats[2],
                           domains_blocked = stats[3]
                        )

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