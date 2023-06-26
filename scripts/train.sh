#!/bin/bash

mkdir /tmp/paw/output --parents

export DATASET_DIR=/tmp/paw/data/current/
export OUTPUT_DIR=/tmp/paw/output/
export WEIGHTS=/tmp/paw/weights/

docker rm -f paw_training
#docker compose build training
docker compose up training -d
docker logs -f paw_training
