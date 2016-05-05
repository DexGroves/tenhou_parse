#!/bin/bash

if [ ! -e data/2013.tar.gz ]
  then
    curl http://arcturus.su/tenhou/gamelogs/houou/2013.tar.gz > data/2013.tar.gz
    tar -zxf data/2013.tar.gz -C data/
fi
