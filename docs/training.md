Training
---

After following the dataset guidelines, please create `.env` file on the root of the project.
The `.env` file should contain all the paths for dataset, weights and output.

```bash
# nano .env, then paste:
DATASET_DIR=<dataset directory>
WEIGHTS=<weights directory> #create a new directory as destination of the downloaded weights
OUTPUT_DIR=<output directory> # create a new directory for saving the training output
```

The training routine is included on the `docker-compose.yaml`,
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

### Usage:
```yaml
python -m app.run.train # run training as a module of `app`
--config ./app/config/train.yaml # consists of the directories and general info about the training
--epochs 32   # number of epochs
--device 0    # either `cpu` or the <gpu-id>
--batch 64    # batch size (for auto-batch -1)
--image_size  #320
```


## Method

### YOLO V8
In this article, we explore the benefits of using YOLO v8, a powerful deep learning model,
for quick segmentation projects. YOLO v8 combines speed and accuracy, making it an excellent
choice for real-time analysis. It offers reliable instance segmentation results without
sacrificing performance and can handle diverse object categories. Additionally, we discuss
how to integrate YOLO v8 with Docker, FastAPI, and Flask for efficient model training and
deployment. Join us as we unlock the potential of YOLO v8 in your instance segmentation endeavors.
