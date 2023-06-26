import numpy as np
import uvicorn
import pydantic
import logging

from os import environ
from typing import Dict

from PIL import Image
from ultralytics import YOLO

from fastapi import FastAPI
from fastapi import Response, status

from schemas.input import InputItem
from schemas.response import ResponseItems

model = YOLO("/weights/best.pt")


app = FastAPI()
VERSION = (
    environ["VERSION"] if "VERSION" in environ and environ["VERSION"] is not None else 1
)


@app.get("/")
def home() -> Dict:
    return {"api": "paw_detective"}


@app.get("/version")
def version() -> Dict:
    return dict(version=VERSION)


@app.post(f"/{VERSION}/predict", response_model=ResponseItems)
def predict(body: InputItem) -> ResponseItems:
    response = model.predict(
        body.input_src, project=body.output_src, save=True, imgsz=320, conf=0.2
    )
    if response is not None:
        print(f"{response=}")
        print(len(response))
        filename = (
            response[0].save_dir.split("/")[-1] + "/" + body.input_src.split("/")[-1]
        )
        try:
            response = [
                dict(
                    breed=str(resp.names[int(resp.boxes.cls.numpy()[0])]),
                    breed_id=int(resp.boxes.cls.numpy()[0]),
                    confidence="{:.2f}".format(float(resp.boxes.conf[0]) * 100),
                    output_src=resp.save_dir.split("/")[-1]
                    + "/"
                    + body.input_src.split("/")[-1],
                )
                for resp in response
            ]
        except Exception:
            response = [dict(output_src=filename)]
        response = pydantic.parse_obj_as(ResponseItems, response)
        logging.info(f"Success on input {body.input_src} and output {body.output_src}")
        return response
    else:
        logging.error(f"Fail on input {body.input_src} and output {body.output_path}")
    return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(f"/{VERSION}/batch_singles/", response_model=Dict)
def batch_singles(samples: int) -> dict[str, float | str]:
    import time

    image_path = "./examples/example.jpg"
    image = np.asarray(Image.open(image_path))
    images = [image + np.random.random()] * samples
    print(len(images))

    start_time = time.time()
    [model(i) for i in images]
    elapsed_time = time.time() - start_time
    return dict(time=elapsed_time, unit="seconds")


@app.get(f"/{VERSION}/batch_stream/", response_model=Dict)
def batch_stream(samples: int) -> dict[str, float | str]:
    import time

    image_path = "./examples/example.jpg"
    image = np.asarray(Image.open(image_path))
    images = [image + np.random.random()] * samples
    print(len(images))

    start_time = time.time()
    model(images, stream=True, save=False)
    elapsed_time = time.time() - start_time
    return dict(time=elapsed_time, unit="seconds")


@app.get("/ping")
def ping() -> str:
    return "Pong"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
