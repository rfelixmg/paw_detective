Training
---

This section covers the training routine, which has been simplified by providing
all the triggers in the Docker Compose. The only remaining task is to set up the
environment directories, allowing the container to save outputs on the host machine
instead of within the Docker environment. To achieve this, we utilize volume binding
for the weights and dataset directories.

### YOLO V8

In this article, we explore the benefits of using YOLO v8, a powerful deep learning model,
for quick segmentation projects. YOLO v8 combines speed and accuracy, making it an excellent
choice for real-time analysis. It offers reliable instance segmentation results without
sacrificing performance and can handle diverse object categories. Additionally, we discuss
how to integrate YOLO v8 with Docker, FastAPI, and Flask for efficient model training and
deployment.


## Getting Started

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/rfelixmg/paw_detective.git
   cd paw_detective
   ```

2. Run `dataset` and `weights` scripts:

    ```bash
   bash ./scripts/dataset.sh
   bash ./scripts/weights.sh
    ```

4. **Variables**: After following the dataset guidelines, please create `.env` file on the root of the project.
The `.env` file should contain all the paths for dataset, weights and output.

    ```bash
    # nano .env, then paste:
    DATASET_DIR=<dataset directory>
    WEIGHTS=<weights directory> #create a new directory as destination of the downloaded weights
    OUTPUT_DIR=<output directory> # create a new directory for saving the training output
    ```

5. **Docker**: The training routine is included on the `docker-compose.yaml`

    ```yaml
    training:
      << : *debug # copy the basic debug container
      container_name: paw_training
      command:
        bash -c "
        pip install -e . && \  # install the project `paw` as a python package
        python -m app.run.train --config ./app/config/train.yaml --epochs 32 --device 0 --batch 64
        "
    ```

## Usage:

```yaml
python -m app.run.train # run training as a module of `app`
--config ./app/config/train.yaml # consists of the directories and general info about the training
--epochs 32   # number of epochs
--device 0    # either `cpu` or the <gpu-id>
--batch 64    # batch size (for auto-batch -1)
--image_size  #320
```

```bash
docker compose build train
docker compose up train
```
