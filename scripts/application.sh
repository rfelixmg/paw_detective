#!/bin/bash

mkdir /tmp/paw/web/{uploads,results} --parents
export DATADIR=/tmp/paw/web/uploads/
export OUTPUTDIR=/tmp/paw/web/results/
export WEIGHTS=/tmp/paw/weights/

docker compose up paw_web paw_api
