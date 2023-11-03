FROM python:3.11.6-alpine3.18

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000