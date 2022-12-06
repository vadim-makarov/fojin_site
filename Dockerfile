FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get install -y chromium-bsu
RUN py.test -n auto
CMD tail -f /dev/null