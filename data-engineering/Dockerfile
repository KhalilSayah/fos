FROM python:3.11.3-alpine
COPY . .
CMD pip install -r requirements.txt  

RUN apt-get update
RUN apt-get -y install cron

RUN crontab -l | { cat; echo "* * * * * python etl.py"; } | crontab -
CMD cron