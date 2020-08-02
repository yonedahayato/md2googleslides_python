FROM python:3.6-slim

ADD . .

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "md2gslides.py"]
