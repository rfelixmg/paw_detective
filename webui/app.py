import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def home() -> render_template:
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def get_results() -> render_template:
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]
    if file.filename == "":
        return "No selected file"
    if file:
        print("Original filename: ", file.filename)  # Add this line
        print("Secure filename: ", secure_filename(file.filename))  # And this line
        filename = secure_filename(file.filename)
        file.save(os.path.join("static/uploads", filename))
        return render_template("results.html", image_filename=filename)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
