FROM registry.access.redhat.com/ubi9/python-312-minimal:latest

COPY app/ /opt/app-root/src/
COPY static/ /opt/app-root/src/
COPY requirements.txt /opt/app-root/src/

RUN pip install -r requirements.txt

CMD uvicorn app.main:app --reload --port 8001