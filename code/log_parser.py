#!/usr/bin/env python2.7

"""
Parse a single tenhou XML and return all ponds and winning tiles
for players who declared riichi and won.
"""

import xml.etree.ElementTree as etree
import urlparse


who_to_defg = {'0': 'D', '1': 'E', '2': 'F', '3': 'G'}


TILES = """
    1s 2s 3s 4s 5s 6s 7s 8s 9s
    1p 2p 3p 4p 5p 6p 7p 8p 9p
    1m 2m 3m 4m 5m 6m 7m 8m 9m
    ew sw ww nw
    wd gd rd
""".split()


def parse_log(log):
    events = etree.parse(log).getroot()

    riichi_wins = []
    all_discards = []
    hand_discards = {'D': [], 'E': [], 'F': [], 'G': []}

    for event in events[4:]:
        if event.tag == "AGARI":
            all_discards.append(hand_discards)

            yaku = extract_yaku(event)

            if has_riichi(yaku):
                winner = who_to_defg[event.attrib['who']]
                winning_tile = convert_tilecode_to_name(event.attrib['machi'])
                riichi_wins.append((winner, winning_tile))
            else:
                riichi_wins.append((None, None))

            hand_discards = {'D': [], 'E': [], 'F': [], 'G': []}
            continue

        if event.tag == "RYUUKYOKU":
            all_discards.append(hand_discards)
            riichi_wins.append((None, None))

            hand_discards = {'D': [], 'E': [], 'F': [], 'G': []}
            continue

        if event.tag == "DORA":
            continue     # Should handle this case in future

        if event.tag[0] in 'DEFG':
            discarded_tile = convert_tilecode_to_name(event.tag[1:])
            hand_discards[event.tag[0]].append(discarded_tile)

    riichi_discards = [all_discards[i] for i in xrange(len(all_discards))
                       if riichi_wins[i] != (None, None)]
    riichi_wins = [wins for wins in riichi_wins if wins != (None, None)]

    return riichi_wins, riichi_discards


def extract_yaku(event):
    """event yaku are tuples of ID, count. Return just IDs."""
    return event.attrib['yaku'].split(',')[::2]


def has_riichi(yaku):
    """Riichi is yaku 1."""
    if '1' in yaku:
        return True
    return False


def convert_tilecode_to_name(tile_cd):
    return TILES[int(tile_cd) // 4]
