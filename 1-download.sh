#!/bin/bash

curl http://arcturus.su/tenhou/gamelogs/houou/2010.tar.gz > data/2010.tar.gz
curl http://arcturus.su/tenhou/gamelogs/houou/2011.tar.gz > data/2011.tar.gz
curl http://arcturus.su/tenhou/gamelogs/houou/2012.tar.gz > data/2012.tar.gz
curl http://arcturus.su/tenhou/gamelogs/houou/2013.tar.gz > data/2013.tar.gz

tar -zxf data/2010.tar.gz -C data/
tar -zxf data/2011.tar.gz -C data/
tar -zxf data/2012.tar.gz -C data/
tar -zxf data/2013.tar.gz -C data/
