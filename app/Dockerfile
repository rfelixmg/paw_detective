FROM ultralytics/ultralytics:latest

COPY requirements.txt /opt/meta/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /opt/meta/requirements.txt

WORKDIR /opt/dev/
