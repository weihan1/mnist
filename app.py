from flask import Flask, render_template, request
from model import preprocess, load_model
import numpy as np


app = Flask(__name__)

model = load_model()

@app.route("/")
def home_page():
    return render_template("user_interface.html")

@app.route("/submit", methods = ['GET', 'POST'])
def output():
    if request.method == "POST":
        img = request.files["my_image"]
        img_path = "test_data/" + img.filename
        img.save(img_path)
        preprocessed_data = preprocess(img_path)
        predict = str(np.argmax(model.predict(preprocessed_data))) #chooses the predicted number with highest probability

        if predict == "11":
            predict = "100"
        elif predict == "12":
            predict = "1000"
        elif predict == "13":
            predict = "10000"
        elif predict == "14":
            predict = "100000000"
    return render_template("user_interface.html", prediction = predict, path = img_path)


        


if __name__ == "__main__":
    app.run(debug=True)


