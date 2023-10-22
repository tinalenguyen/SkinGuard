from flask import Flask, request, render_template, redirect, session
from roboflow import Roboflow

rf = Roboflow(api_key="8CUbAAkdfWfm2vpOmv2n")
project = rf.workspace().project("melanoma-cancer")
model = project.version(1).model

# # infer on a local image
# print(model.predict("melanomaexp.jpeg", confidence=40, overlap=30).json())

# # visualize your prediction
# model.predict("melanomaexp.jpeg", confidence=40, overlap=30).save("prediction.jpg")


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

@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template("test.html")
    
@app.route("/submit")
def submit():
    inputVal = request.args.get("inputVal")
    model.predict(inputVal, confidence=40, overlap=30).save("prediction.jpg")
    

    # rest of the code
if __name__ == "__main__": 
    app.debug = True
    app.run()