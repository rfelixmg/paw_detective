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
        results = dict(
            breed="Staffordshire Bull Terrier", confidence=0.96 * 100, mask=[]
        )
        filename = "no_sample_example.jpg"
    else:
        results = dict(
            breed="Staffordshire Bull Terrier", confidence=0.96 * 100, mask=[]
        )

        filename = secure_filename(file.filename)
        file.save(os.path.join("static/uploads", filename))

    return render_template("results.html", image_filename=filename, results=results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
