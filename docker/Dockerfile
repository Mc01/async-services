FROM python:alpine

RUN apk add --update --no-cache make gcc g++ libffi-dev

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.py /entrypoint.py

WORKDIR /app
