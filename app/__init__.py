from flask import Flask, request, render_template, redirect, session

from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "skin"

def logged_in():
    return "user" in session

@app.route("/", methods=['GET', 'POST'])
def welcome():
    return redirect("/start")


@app.route("/start", methods=['GET', 'POST'])
def start():
    return render_template("start.html")

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


if __name__ == "__main__": 
    app.debug = True
    app.run()