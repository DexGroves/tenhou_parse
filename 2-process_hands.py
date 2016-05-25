"""
Process XML supplied by commandline argument and process.
For each completed riichi hand, output one line to stdout as:
    [winning tile] [padded winner pond] [consumed tiles]
"""

from __future__ import print_function
from code.log_parser import parse_log
from code.win_encoder import encode_win_details
import sys
import re
import os


year = '2013'
outfile = open('data/processed/' + year + '.csv', 'a')

for logfile in os.listdir('data/' + year):
    if not re.search('00a9', logfile) or re.search('00e1', logfile):
        continue

    try:
        logfile_nm = 'data/' + year + '/' + logfile

        riichi_wins, riichi_discards = parse_log(open(logfile_nm))

        print('.', end = '')

        for i, win_details in enumerate(riichi_wins):
            encoded_hand = encode_win_details(win_details, riichi_discards[i])
            print(*encoded_hand, sep=',', file=outfile)

    except:
        pass
