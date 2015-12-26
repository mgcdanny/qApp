FROM rabbitmq:latest
MAINTAINER Daniel Gabrieli

RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN chmod 0755 /var/run/sshd

RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY rmq.sh /etc/supervisor/conf.d/rmq.sh

RUN apt-get install -y vim

CMD ["/usr/bin/supervisord"]
