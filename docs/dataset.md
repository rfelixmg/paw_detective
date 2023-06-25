# Cats and dogs `dataset`

## Processed dataset

```bash
wget https://tinyurl.com/msvwtpzw
unzip cats_and_dogs.zip -o cats_and_dogs/

DATASET_DIR=$PWD/cats_and_dogs/

# or un-comment line 22 on docker-compose.yml and:
export DATASET_DIR=$PWD/cats_and_dogs/
```

## Downloading & Processing the dataset

```bash
wget https://tinyurl.com/msvwtpzw
unzip cats_and_dogs.zip -o cats_and_dogs/

DATASET_DIR=$PWD/cats_and_dogs/

# or un-comment line 22 on docker-compose.yml and:
export DATASET_DIR=$PWD/cats_and_dogs/
```

Use your bash to to print the following line:
```bash
echo $DATASET_DIR:/data/
# example output: /home/smith/cats_and_dogs/:/data/
```


The result should be added to the section `volumes` on your `docker-compose.yml`:

## Processing dataset

The `docker-compose` file contains a routine for processing the dataset.
It leverages the folder `/data/` and the existent configs on `app/config`

```yaml
    # lines 32-39 `docker-compose.yaml`
    data2pipeline:
      << : *debug #copy debug configurations
      container_name: paw_data2pipeline
      command:
        bash -c "
        pip install -e . && \  # this installs the project as a python package
        python -m app.run.data2pipeline -c ./app/config/train.yaml --singles
        "
```

For running the task, please:
```bash
docker compose up data2pipeline --build
#or
docker compose build data2pipeline
docker compose up data2pipeline
```
