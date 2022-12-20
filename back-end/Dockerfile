FROM python

WORKDIR /home
COPY source/ .
COPY back-end/requirements.txt .

RUN apt-get update && apt-get install -y vim
RUN apt install python3-pip -y
RUN pip install -r requirements.txt
