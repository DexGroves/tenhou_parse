#!/usr/bin/env python2.7

"""
Parse a single tenhou XML and return all ponds and winning tiles
for players who declared riichi and won.
"""

import xml.etree.ElementTree as etree
import urlparse


who_to_defg = {'0': 'D', '1': 'E', '2': 'F', '3': 'G'}

def parse_log(log):
    events = etree.parse(log).getroot()

    wins = []
    all_discards = []
    discards = {'D': [], 'E': [], 'F': [], 'G': []}

    for event in events:
        if event.tag == 'AGARI':
            all_discards.append(discards)

            yaku = extract_yaku(event)

            if has_riichi(yaku):
                winner = who_to_defg[event.attrib['who']]
                winning_tile = event.attrib['machi']
                wins.append((winner, winning_tile))
            else:
                wins.append((None, None))

            discards = {'D': [], 'E': [], 'F': [], 'G': []}
            next

        if event.tag == "RYUUKYOKU":
            all_discards.append(discards)
            wins.append((None, None))

            discards = {'D': [], 'E': [], 'F': [], 'G': []}
            next

        if event.tag[0] in 'DEFG':
            discards[event.tag[0]].append(event.tag[1:])

    return wins, all_discards

def extract_yaku(event):
    """event yaku are tuples of ID, count. Return just IDs."""
    return event.attrib['yaku'].split(',')[::2]

def has_riichi(yaku):
    """Riichi is yaku 1."""
    if '1' in yaku:
        return True
    return False
