import numpy as np
from itertools import chain


TILES = """
    1s 2s 3s 4s 5s 6s 7s 8s 9s
    1p 2p 3p 4p 5p 6p 7p 8p 9p
    1m 2m 3m 4m 5m 6m 7m 8m 9m
    ew sw ww nw
    wd gd rd
""".split()


MAX_POND_LEN = 18


def encode_win_details(win_details, discards):
    """
    Encode the gamestate at point of win as an integer list:
        [winning tile] [winning pond] [consumed tiles]
    winning tile as an index
    winning pond as:  index = chronology, value = tile_index
    consumed tile as: index = tile_index, value = count
    """
    winner = win_details[0]
    winning_tile = win_details[1]
    winning_pond = discards[winner]
    all_discards = discards.values()

    winning_tile_idx = TILES.index(winning_tile)
    winning_pond_idx = [TILES.index(tile) for tile in winning_pond]

    padded_pond = pad_pond(winning_pond_idx, MAX_POND_LEN)
    consumed_tiles = count_consumed_tiles(chain(*all_discards))

    return [winning_tile_idx] + list(padded_pond) + list(consumed_tiles)


def pad_pond(pond, length):
    if len(pond) > length:
        return pond[0:length]
    return pond + [-1] * (length - len(pond))


def count_consumed_tiles(tiles):
    tile_count = np.zeros(len(TILES), dtype=int)
    for tile in tiles:
        tile_count[TILES.index(tile)] += 1
    return tile_count
