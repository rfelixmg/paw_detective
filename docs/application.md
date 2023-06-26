Web application
---

---
**TL;DR**: For running the application with our pre-trained models:
   ```bash
   bash ./scripts/weights.sh # download the weights
   bash ./scripts/application.sh # load Flask + fastapi
   ```
---

## Getting started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rfelixmg/paw_detective.git
   cd paw_detective
   ```

2. Download weights

    ```bash
    mkdir weights
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=144dVCpxYt2xWSpyjNKYtvgm4F2VRR1l2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=144dVCpxYt2xWSpyjNKYtvgm4F2VRR1l2" -O weights/best.pt && rm -rf /tmp/cookies.txt
    export WEIGHTS=$PWD/weights/
    ```

3. Run docker compose

    ```bash
   docker compose build paw_api paw_web
   docker compose up paw_api paw_web
    ```

## Limitations

## Structure
