#!/bin/bash

mkdir /tmp/paw/weights/ --parents
export WEIGHTS=/tmp/paw/weights/

cd /tmp/paw/weights/
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1p3HxN6ZY_Hl5MgVnSwbWYlnyOQ1OmPpN' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1p3HxN6ZY_Hl5MgVnSwbWYlnyOQ1OmPpN" -O best.pt && rm -rf /tmp/cookies.txt
