FROM python

RUN apt-get update && apt-get install -y vim

RUN apt install python3-pip -y

COPY requirements.txt .
RUN pip install -r requirements.txt
