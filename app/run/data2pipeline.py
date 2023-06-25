import argparse
import logging
import os
import shutil
from typing import Dict

import cv2
import yaml

from tqdm import tqdm
from sklearn.model_selection import train_test_split

from paw.schemas.dataloader import AnnotationItems
from paw.dataloader.mask import mask2segmentation


def mkdirs(split: str) -> None:
    try:
        for dir in ("images", "labels", "masks"):
            os.makedirs(f"/data/{split}/{dir}/", exist_ok=True)
    except Exception:
        pass


def get_class2id(filepath: str) -> Dict:
    with open(filepath, "r") as file:
        statics = yaml.safe_load(file)
        class2id = {value: key for key, value in statics["names"].items()}
    return class2id


def main() -> None:
    # Loading annotation
    annotation_path = "/data/pets_dataset_info.csv"
    annotations = AnnotationItems.from_csv(annotation_path)

    if args.singles:
        logging.warning("Using single annotations only")
        annotations = [ann for ann in annotations if len(ann.pet_id) == 1]

    # Splitting dataset
    train, _ = train_test_split(annotations, test_size=0.4)
    val, test = train_test_split(_)
    print("number samples per split:", len(train), len(val), len(test))
    class2id = get_class2id(args.config)

    for split, samples in {"train": train, "val": val, "test": test}.items():
        mkdirs(split)
        for sample in tqdm(samples):
            # copying files
            shutil.copy(
                f"/data/data/{sample.id}/image.jpg",
                f"/data/{split}/images/{sample.id}.jpg",
            )
            shutil.copy(
                f"/data/data/{sample.id}/mask.jpg",
                f"/data/{split}/masks/{sample.id}.jpg",
            )

            # Extracting countor
            mask_path = f"/data/data/{sample.id}/mask.jpg"
            segmentations = mask2segmentation(mask_path)
            image = cv2.imread(f"/data/{split}/masks/{sample.id}.jpg", 0)[
                :, :, None
            ].repeat(3, -1)
            contour_image = cv2.drawContours(
                image, segmentations, -1, (0, 0, 255), thickness=3
            )
            filepath = f"/data/{split}/masks/{sample.id}_contour.jpg"
            cv2.imwrite(filepath, contour_image)

            # Converting contour to flat list
            with open(f"/data/{split}/labels/{sample.id}.txt", "w") as fp:
                for pid, segmentation in zip(sample.breed, segmentations):
                    seg = " ".join([str(i) for i in segmentation.flatten()])
                    fp.write(f"{class2id[pid]} {seg}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("data2pipeline")

    parser.add_argument("--config", default="./app/config/train.yaml", type=str)
    parser.add_argument(
        "--singles", help="Use single instances only", action="store_true"
    )
    args = parser.parse_args()

    main()
