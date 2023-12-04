FROM python:3.8-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    gcc \
    libasound2-dev \
    portaudio19-dev \
    flac \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY . .

ENV NAME mlclientdocker
