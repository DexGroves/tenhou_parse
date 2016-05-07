#!/bin/bash


for file in `ls data/2013 | grep 00a9`
  do
    printf .
    ./code/process_hands.py data/2013/$file >> data/processed/2013.csv
  done
