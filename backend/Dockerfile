FROM python:3.11.4-slim-buster

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip


COPY ./requirements.txt /usr/src/backend/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/backend/requirements.txt

COPY . /usr/src/backend/

