# in production this should probably be busybox, but let's use ubuntu for a
# fair comparison 
FROM tutum/ubuntu

MAINTAINER Ram Rajamony, rajamon@us.ibm.com

COPY gups.c /
COPY utils.c /
COPY utils.h /
COPY RandomAccess.h /
RUN gcc -Wall -g -c utils.c
RUN gcc -Wall -g -c gups.c
RUN gcc -o gups utils.o gups.o -lm
CMD sudo apt-get update -y
CMD sudo apt-get install -y libgomp1
CMD sudo apt-get install -y numactl
# RUN apt-get -qq install -y libgomp1 numactl
# WORKDIR /Users/bfont/Desktop/kvm-docker-comparison/RandomAccess
# ADD bin / 
# CMD numactl --physcpubind=0-7,16-23 --localalloc /gups.c
CMD ./gups
CMD exit
