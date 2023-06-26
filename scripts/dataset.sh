#!/bin/bash

mkdir /tmp/paw/data/{current,raw} --parents
cd /tmp/paw/data/
# Download processed dataset
wget <web-link>
unzip cats_and_dog_dataset.zip -o current/
export DATASET_DIR=/tmp/paw/data/current/

# Download non-processed dataset
#wget <web-link>
#unzip cats_and_dog.zip -o raw/
#export DATASET_DIR=/tmp/paw/data/raw/
#docker compose up data2pipeline --build
