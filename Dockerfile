FROM python:3.8

ENV PORT 5000
ENV HOST 0.0.0.0

EXPOSE 5000

WORKDIR /

RUN apt-get update -y && \
    apt-get install -y python3-pip

RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD app.py .
ADD convert.py .

ADD download.py .
RUN python3 download.py

ADD function.py .


ENTRYPOINT ["python", "app.py"]
