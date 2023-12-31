# Paw Detective

Paw Detective is a pet detection system that utilizes Ultralytics and YOLOv8 to detect
and classify various pet breeds in images. This repository provides a complete training
pipeline, data processing utilities, and a Flask application for online interaction with
the trained model. For a more informative discussion on the project, please refer to
[Flask & fastapi application](./docs/application.md).

Supports:
```yaml
architecture: x86_64
```


# TL;DR <a name="tldr"></a>

You might prefer to use a more straightforward approach to reproduce the project using [**scripts**](./docs/scripts.md).
### Training:
1. [Dataset configuration](./docs/dataset.md)
2. [Weights](./docs/weights.md)
3. [Training model](./docs/training.md)
4. [Flask & fastapi application](./docs/application.md)




> Home Page
>
> ![Home](./docs/src/home.png)

> Results page
>
> ![Home](./docs/src/response.png)


## Dataset

There area comprehensive pet dataset called the Oxford-IIIT Pet dataset. It consists of 37 different pet categories,
with approximately 200 images available for each class. The dataset is diverse, with variations in scale, pose, and
lighting across the images. Each image in the dataset is accompanied by ground truth annotations, including breed
information, head region of interest (ROI), and pixel-level trimap segmentation.

To download the dataset and annotations please refer to the section [Dataset configuration](./docs/dataset.md).

## Repository Structure


The "paw_detective" repository is structured as follows:

```bash
paw_detective/
├── api/
│ ├── app.py
├── app/
│ ├── run/
│ │ ├── data2pipeline.py
│ │ ├── train.py
├── docs/
│ ├── annotations/
├── scripts/
│ ├── dataset.sh
│ ├── train.sh
│ ├── application.sh
│ ├── weights.sh
├── src/
│ ├── paw/
├── webui/
│ ├── app.py
├── README.md
├── docker-compose.yaml
└── requirements.txt
```

The main components of the repository are as follows:

- **webui/**: The `Flask application` resides in this directory. It provides an interface for interacting with the trained model.
- **api/**: A `fastapi` application that allows to run scalable predictions.
- **src/paw/**: This directory includes the source code for data processing, training pipeline, and other utilities.
- **README.md**: This file, which you are currently reading, provides an overview of the project and instructions for setup.
- **requirements.txt**: It lists all the required Python packages and their versions for running the code.

## Getting Started

To use the Paw Detective system, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rfelixmg/paw_detective.git
   cd paw_detective
   ```

2. Use docker-compose for building all the images:

   - `.env` file:
   ```bash
   # Training .env
   DATASET_DIR=   # processed dataset directory {train, val, test} sub-folders
   WEIGHTS=       # directory to save YoLOV8 pre-trained weights
   OUTPUT_DIR=    # directory to save ultralytics training

   # Application .env
   DATADIR=       #directory for Flask upload images
   OUTPUTDIR=     #directory for Flask result images
   WEIGHTS=       #directory with latest weights (best.pt)
   ```

   ```bash
   docker compose build
   ```

3. Refer to the section [TL;DR](#tldr) to setup the environment, or use the following scripts.

   For running the application with our pre-trained models:
   ```bash
   bash ./scripts/weights.sh
   bash ./scripts/application.sh
   ```

   For fine-tunning and running the application:

   ```bash
   bash ./scripts/dataset.sh
   bash ./scripts/weights.sh
   bash ./scripts/train.sh
   bash ./scripts/application.sh
   ```

4. Access the Flask web application to test the model's performance

   > http://localhost:5001              # Flask
   >
   > http://localhost:7000/docs#        #fastapi


## Machine Configurations

The following machine configurations were used for training, and testing of the first version of this repository.

```yaml
  nvidia: NVIDIA-SMI 515.105.01
  driver: 515.105.01
  cuda: 11.7
  gpu: NVIDIA GeForce RTX 3070 Laptop GPU, 7982MiB
  distribution: Ubuntu
  distribution.version: 22.04
  distribution.name: jammy
  distribution.description: Ubuntu 22.04 LTS
```

# Results

Please refer to the page [Results](./docs/results.md) for a comprehensive view of the models' performance.

### References
1. [Towards Data Science](https://towardsdatascience.com/trian-yolov8-instance-segmentation-on-your-data-6ffa04b2debd)
2. [Ultralytics](https://docs.ultralytics.com/datasets/segment/)
3. [Learn OpenCV](https://learnopencv.com/train-yolov8-on-custom-dataset/)
