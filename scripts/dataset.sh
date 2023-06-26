#!/bin/bash

mkdir /tmp/paw/data/{current,raw} --parents
cd /tmp/paw/data/
# Download processed dataset
echo "Downloading processed dataset -- it might take a while (1 GB)...";
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1FkO7Zj3hx_7FhrfUXDo3Zzsz_NjqA8Eg' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1FkO7Zj3hx_7FhrfUXDo3Zzsz_NjqA8Eg" -O cats_and_dogs_dataset.zip && rm -rf /tmp/cookies.txt
unzip cats_and_dog_dataset.zip -d current/
export DATASET_DIR=/tmp/paw/data/current/

# Download non-processed dataset
#wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1o45kLDLQBox1uk6wcM_F4hwwgg0pI7G' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1o45kLDLQBox1uk6wcM_F4hwwgg0pI7G" -O cats_and_dogs.zip && rm -rf /tmp/cookies.txt
#unzip cats_and_dog.zip -o raw/
#export DATASET_DIR=/tmp/paw/data/raw/
#docker compose up data2pipeline --build
