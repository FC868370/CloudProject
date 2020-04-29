#!/bin/bash
gcc -O stream.c -o stream
mkdir -p results
log="results/docker.log"
now=`date`
echo "Running Stream Benchmark. Started at $now"
echo "-----------------------------------------------------------------"
echo "Running Stream Benchmark. Started at $now" >> $log
for i in `seq 20`; do ./stream >> $log; done
echo -n "Stream Benchmark completed at "; date
