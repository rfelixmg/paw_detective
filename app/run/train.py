import argparse
from typing import Any

from ultralytics import YOLO


def main() -> Any:
    model = YOLO("yolov8n-seg.pt")
    results = model.train(
        batch=args.batch,
        device="cpu",
        data=args.config,
        epochs=args.epoch,
        imgsz=args.image_size,
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
    parser.add_argument("--epoch", type=int, default=32)
    parser.add_argument("--batch", type=int, default=32)
    parser.add_argument("--image_size", type=int, default=224)
    args = parser.parse_args()

    main()
