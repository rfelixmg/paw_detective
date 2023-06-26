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

## Discussions


I have been eager to explore the functionalities of the new YoLO v8 powered by Ultralytics.
Unfortunately, I haven't had much time to work on a simple application incorporating all of
its features. However, I recently took some time to experiment with YoLO V8, and I found it
to be remarkably straightforward.

The current version of YoLO V8 utilizes PyTorch as its underlying framework, which proves
to be highly efficient for training the model. One notable advantage is that the model is
capable of automatically determining the appropriate learning rate and batch size. Additionally,
when adhering to the specific train/test/validation setup defined by the framework, the entire
process becomes very intuitive.



1. **Architectural choice:**

   Regarding the architectural choices, the current repository consists of five components.
   > **A. Docker container**: All the subsequent components have been implemented using Docker
   containers as the foundation. This approach is aimed at enhancing reproducibility and
   simplifying the setup process. For simplicity, we have added all the features with docker-compose.

   > B. **src/paw**: This component is a straightforward Python package (PyPI) that encompasses essential
   functionalities for data processing, storing important schemas, and utility methods. The purpose of
   this package is to offer all the necessary functionalities required by the `app` component. One
   notable aspect of `paw` is its easy installation using `pip`, enabling convenient access from any
   process within the Docker container.

   > **C. app**: This component encompasses simple routines for all training-related tasks, such as data
   processing and training pipelines. It provides a straightforward structure to handle various aspects
   of the training process efficiently.

   > **D. api**: This component is built using FastAPI, providing a convenient interface for accessing
   model predictions. The API is designed to be easily deployed on cloud infrastructure, and it can
   be effortlessly adapted to serverless instances, offering potential cost savings.

   > **E. webui**: This component is a basic Flask application designed to showcase the model. It
   provides a user-friendly web interface where the model's capabilities can be demonstrated.


4. **Model's performance:**

   We developed two methods to evaluate the performance of the model given large batch processing tasks.
   For both tasks, we abstracted the loading tasks of the images to the model for simplicity. This is based
   on the assumption that the client side could potentially be operating in this. Given that the application
   was developed using `fastapi`, this structure could be easily leverage using the AWS cloud (or similar)
   for scalable process. Given the current rate 25 fps, to process a large batch (e.g. 8K+) it would be required
   a infrastructure with at least 320 serverless instances.
   ```bash
   serverless (8192 Gb): $0.0000001333 per ms (a)
   Number of units: 320 units (b)
   Timeframe: 1000 ms (c)
   cost_per_second = a * b *c
   Cost per second for larger batches: $0.042656 + \var
   ```
5. **Solutions:**
   > `localhost:7000/batch_singles/samples=<NUMBER>`
   >
   > - samples determine the number of times the sample image will be repeated
   > - This `entrypoint` refers to executing each sample in a loop, and it's performance behaves in
   >    average `40` miliseconds.

   > `localhost:7000/batch_stream/samples=<NUMBER>`
   >
   > - samples determine the number of times the sample image will be repeated
   > - This `entrypoint` refers to executing frames in a stream, and leverages previous predictions to speed
   > the prediction steps (in-built on ultralytics).
