import os
import shutil
from typing import Any

import requests  # type: ignore

from flask import Flask, render_template, request, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


def copy(src: str, dst: str) -> None:
    if os.path.islink(src):
        linkto = os.readlink(src)
        os.symlink(linkto, dst)
    else:
        shutil.copy(src, dst)


def api_request(filename: str) -> Any:
    data = {"input_src": filename, "output_src": "/results/"}
    worker_url = "http://paw_api:7000/1/predict"
    return requests.post(url=worker_url, json=data).json()


@app.route("/")
def home() -> render_template:
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def get_results() -> render_template:
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    app.logger.info(f"{file.filename=}")
    if file.filename == "":
        filename = "example.jpg"
        copy("/app/static/images/example.jpg", "/uploads/example.jpg")
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join("/uploads", filename))
        copy(f"/uploads/{filename}", f"/app/static/uploads/{filename}")

    results = api_request(os.path.join("/uploads", filename))
    app.logger.info(results)
    fname = results[0]["output_src"]
    copy(f"/results/{fname}", "/app/static/results/")

    response = make_response(
        render_template("results.html", image_filename=filename, results=results)
    )
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
    # return render_template("results.html", image_filename=filename, results=results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
