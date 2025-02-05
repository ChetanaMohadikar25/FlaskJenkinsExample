#FROM python:3.14.0a2-slim
FROM python:3.14.0a2-slim
WORKDIR /flaskapp

COPY app.py /flaskapp/

RUN pip install -r requirements.txt

CMD ["python","app.py"]