FROM python:latest
MAINTAINER Daniel Gabrieli

RUN echo "deb http://cran.us.r-project.org/bin/linux/debian jessie-cran3/" >> /etc/apt/sources.list

RUN apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y r-base

#too slow for now
#RUN R -e "install.packages(c('data.table', 'digest', 'dplyr', 'gbm', 'hash', 'Imap', #'jsonlite', 'lubridate', 'magrittr', 'nnet', 'plyr', 'randomForest', 'rjson', 'RJSONIO', #'RUnit', 'stringr', 'survival', 'testthat', 'tidyr', 'zipcode', 'zoo', 'caret', #'Rserve'), repos='http://cran.us.r-project.org')"

RUN apt-get install -y vim

RUN mkdir -p /usr/src/web_app
WORKDIR /usr/src/web_app

COPY requirements.txt /usr/src/web_app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/web_app

RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY web_app.sh /etc/supervisor/conf.d/web_app.sh

CMD ["/usr/bin/supervisord"]
# CMD ["celery", "worker", "-A", "app.celery", "-l", "INFO"]
