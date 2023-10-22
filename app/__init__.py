from flask import Flask, request, render_template, redirect, session
from roboflow import Roboflow



# # infer on a local image
# print(model.predict("melanomaexp.jpeg", confidence=40, overlap=30).json())

# # visualize your prediction
# model.predict("melanomaexp.jpeg", confidence=40, overlap=30).save("prediction.jpg")


app = Flask(__name__)
app.secret_key = "skin"
photos = UploadSet('photos', IMAGES)

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
    if (request.method == 'POST'):
        inputVal = request.form.get("fileInput")

        rf = Roboflow(api_key="8CUbAAkdfWfm2vpOmv2n")
        project = rf.workspace().project("melanoma-cancer")
        model = project.version(1).model

        model.predict(inputVal, confidence=40, overlap=30).save("prediction.jpg")
        return redirect("/results")
    
    else:
        return render_template("test.html")
    
@app.route("/results", methods=['GET', 'POST'])
def results():
    return render_template("result.html")
    # rest of the code
if __name__ == "__main__": 
    app.debug = True
    app.run()