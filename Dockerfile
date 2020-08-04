FROM python:3.6-slim

ADD . .

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN dpkg -i pandoc-2.10.1-1-amd64.deb
