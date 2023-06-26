# Cats and dogs `dataset`

## Processed dataset

To download and extract the processed dataset, run the following commands in your terminal:

```bash
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1FkO7Zj3hx_7FhrfUXDo3Zzsz_NjqA8Eg' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1FkO7Zj3hx_7FhrfUXDo3Zzsz_NjqA8Eg" -O cats_and_dogs_dataset.zip && rm -rf /tmp/cookies.txt
mkdir cats_and_dogs/
unzip cats_and_dogs_dataset.zip -d cats_and_dogs/

DATASET_DIR=$PWD/cats_and_dogs/

# or un-comment line 22 on docker-compose.yml and:
export DATASET_DIR=$PWD/cats_and_dogs/
```

Make sure to replace `DATASET_DIR` with the appropriate directory path.

## Downloading & Processing the dataset

To download and extract the dataset, use the following commands:


```bash
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1o45kLDLQBox1uk6wcM_F4hwwgg0pI7G' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1o45kLDLQBox1uk6wcM_F4hwwgg0pI7G" -O cats_and_dogs.zip && rm -rf /tmp/cookies.txt
unzip cats_and_dogs.zip -d cats_and_dogs/

DATASET_DIR=$PWD/cats_and_dogs/

# or un-comment line 22 on docker-compose.yml and:
export DATASET_DIR=$PWD/cats_and_dogs/
```

Again, replace `DATASET_DIR` with the desired directory path.

Use your bash to print the following line:
```bash
echo $DATASET_DIR:/data/
# example output: /home/smith/cats_and_dogs/:/data/
```
The resulting output should be added to the `volumes` section in your `docker-compose.yaml` file.

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

To run the task, please execute the following command:

```bash
docker compose up data2pipeline --build
#or
docker compose build data2pipeline
docker compose up data2pipeline
```

Make sure you are in the appropriate directory and have Docker Compose installed.
