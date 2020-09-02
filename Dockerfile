FROM python:3.8
RUN apt-get update && apt-get -y upgrade

WORKDIR /tmp
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /linkorage
COPY . .

ENV PYTHONPATH="/linkorage"
EXPOSE 5000

