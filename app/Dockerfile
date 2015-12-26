FROM python:latest
MAINTAINER Daniel Gabrieli

RUN echo "deb http://cran.us.r-project.org/bin/linux/debian jessie-cran3/" >> /etc/apt/sources.list

RUN apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y r-base

RUN R -e "install.packages(c('data.table', 'digest', 'dplyr', 'gbm', 'hash', 'Imap', 'jsonlite', 'lubridate', 'magrittr', 'nnet', 'plyr', 'randomForest', 'rjson', 'RJSONIO', 'RUnit', 'stringr', 'survival', 'testthat', 'tidyr', 'zipcode', 'zoo', 'caret', 'Rserve'), repos='http://cran.us.r-project.org')"

RUN apt-get install -y vim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["celery", "worker", "-A", "mytasks", "-l", "INFO"]
