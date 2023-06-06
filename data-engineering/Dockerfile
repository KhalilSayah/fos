FROM python:3.11.3-alpine
COPY requirements.txt requirements.txt 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt  
COPY ..
RUN apt-get update
RUN apt-get -y install cron

RUN crontab -l | { cat; echo "* * * * * python etl.py"; } | crontab -
CMD cron