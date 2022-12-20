FROM python

COPY back-end/ /home/

RUN apt-get update && apt-get install -y vim
RUN apt install python3-pip -y
RUN pip install -r requirements.txt
