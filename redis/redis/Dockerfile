FROM busybox
FROM ubuntu

RUN apt-get update
RUN apt-get install -y redis-server

RUN useradd -m redisuser -s /bin/bash
RUN echo 'redisuser:screencas' | chpasswd

EXPOSE 22
EXPOSE 6379

ADD supervisor.conf /etc/supervisor.conf
cmd [ "/usr/bin/supervisord", "-c", "/etc/supervisor.conf" ]



