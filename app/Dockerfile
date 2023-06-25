FROM ultralytics/ultralytics:latest-python

COPY requirements.txt /opt/meta/
RUN python -m pip install -r /opt/meta/requirements.txt

WORKDIR /opt/dev/
