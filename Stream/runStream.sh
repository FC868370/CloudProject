#!/bin/bash
gcc -O stream.c -o stream
for i in `seq 20`; do ./stream; done
