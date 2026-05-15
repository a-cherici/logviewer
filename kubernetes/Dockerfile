FROM registry.access.redhat.com/ubi9/python-312-minimal:latest

COPY app/ /opt/app-root/src/app
COPY static/ /opt/app-root/src/static
COPY requirements.txt /opt/app-root/src/

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]