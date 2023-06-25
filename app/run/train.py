import argparse
import os
from typing import Any
from ultralytics import YOLO
from paw.utils import experiments


def main() -> Any:
    experiment_path = f"/output/{experiments.name_generator()}"
    os.makedirs(experiment_path, exist_ok=True)

    model = YOLO("/weights/yolov8n-seg.pt")
    results = model.train(
        batch=args.batch,
        device=args.device,
        data=args.config,
        epochs=args.epochs,
        imgsz=args.image_size,
        project=experiment_path,
        workers=0,
    )
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser("train")
    parser.add_argument(
        "--config",
        help="Config file for training (`./app/config/{file}.yaml`)",
        type=str,
        required=True,
    )
    parser.add_argument("--epochs", type=int, default=32)
    parser.add_argument("--batch", type=int, default=32)
    parser.add_argument("--device", type=str, default="cpu")
    parser.add_argument("--image_size", type=int, default=320)
    args = parser.parse_args()

    main()
