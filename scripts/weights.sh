#!/bin/bash

mkdir /tmp/paw/weights/ --parents
export WEIGHTS=/tmp/paw/weights/

cd /tmp/paw/weights/
# trained for 32 epochs
#wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1p3HxN6ZY_Hl5MgVnSwbWYlnyOQ1OmPpN' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1p3HxN6ZY_Hl5MgVnSwbWYlnyOQ1OmPpN" -O best.pt && rm -rf /tmp/cookies.txt

# trained for 512 epochs
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=144dVCpxYt2xWSpyjNKYtvgm4F2VRR1l2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=144dVCpxYt2xWSpyjNKYtvgm4F2VRR1l2" -O best.pt && rm -rf /tmp/cookies.txt
