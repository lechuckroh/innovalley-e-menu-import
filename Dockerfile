FROM python:3.8

COPY . /app
WORKDIR /app

VOLUME ["/app/data"]

RUN pip install -r requirements.txt

CMD python main.py import data
