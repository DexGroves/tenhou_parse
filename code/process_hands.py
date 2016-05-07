#!/usr/bin/env python2.7

"""
Process XML supplied by commandline argument and process.
For each completed riichi hand, output one line to stdout as:
    [winning tile] [padded winner pond] [consumed tiles]
"""

from __future__ import print_function
from log_parser import parse_log
from win_encoder import encode_win_details
import sys


riichi_wins, riichi_discards = parse_log(open(sys.argv[1]))

for i, win_details in enumerate(riichi_wins):
    encoded_hand = encode_win_details(win_details, riichi_discards[i])
    print(*encoded_hand, sep=',')
