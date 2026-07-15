#!/usr/bin/env python3
"""Deterministic I Ching cast utility for the fortune-divination skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import random


TRIGRAMS = {
    (1, 1, 1): ("Qian", "Heaven"),
    (0, 0, 0): ("Kun", "Earth"),
    (1, 0, 0): ("Zhen", "Thunder"),
    (0, 1, 1): ("Xun", "Wind/Wood"),
    (0, 1, 0): ("Kan", "Water"),
    (1, 0, 1): ("Li", "Fire"),
    (0, 0, 1): ("Gen", "Mountain"),
    (1, 1, 0): ("Dui", "Lake"),
}

TRIGRAM_ORDER = [
    (1, 1, 1),  # Qian
    (1, 1, 0),  # Dui
    (1, 0, 1),  # Li
    (1, 0, 0),  # Zhen
    (0, 1, 1),  # Xun
    (0, 1, 0),  # Kan
    (0, 0, 1),  # Gen
    (0, 0, 0),  # Kun
]

KING_WEN_TABLE = [
    [1, 43, 14, 34, 9, 5, 26, 11],
    [10, 58, 38, 54, 61, 60, 41, 19],
    [13, 49, 30, 55, 37, 63, 22, 36],
    [25, 17, 21, 51, 42, 3, 27, 24],
    [44, 28, 50, 32, 57, 48, 18, 46],
    [6, 47, 64, 40, 59, 29, 4, 7],
    [33, 31, 56, 62, 53, 39, 52, 15],
    [12, 45, 35, 16, 20, 8, 23, 2],
]

HEXAGRAM_INFO = {
    1: ("Qian", "creative force, initiative"),
    2: ("Kun", "receptivity, support"),
    3: ("Zhun", "difficult beginning"),
    4: ("Meng", "learning, inexperience"),
    5: ("Xu", "waiting"),
    6: ("Song", "conflict"),
    7: ("Shi", "discipline, collective force"),
    8: ("Bi", "alliance"),
    9: ("Xiao Chu", "small restraint"),
    10: ("Lu", "careful conduct"),
    11: ("Tai", "flow, harmony"),
    12: ("Pi", "blockage"),
    13: ("Tong Ren", "fellowship"),
    14: ("Da You", "great possession"),
    15: ("Qian/Modesty", "modesty"),
    16: ("Yu", "enthusiasm"),
    17: ("Sui", "following"),
    18: ("Gu", "repairing decay"),
    19: ("Lin", "approach"),
    20: ("Guan", "observation"),
    21: ("Shi He", "biting through"),
    22: ("Bi/Grace", "grace, adornment"),
    23: ("Bo", "splitting apart"),
    24: ("Fu", "return"),
    25: ("Wu Wang", "innocence"),
    26: ("Da Chu", "great restraint"),
    27: ("Yi/Nourishment", "nourishment"),
    28: ("Da Guo", "great pressure"),
    29: ("Kan", "repeated risk"),
    30: ("Li", "clarity"),
    31: ("Xian", "influence"),
    32: ("Heng", "endurance"),
    33: ("Dun", "retreat"),
    34: ("Da Zhuang", "great power"),
    35: ("Jin", "progress"),
    36: ("Ming Yi", "hidden light"),
    37: ("Jia Ren", "family/order"),
    38: ("Kui", "opposition"),
    39: ("Jian", "obstruction"),
    40: ("Jie/Release", "release"),
    41: ("Sun", "decrease"),
    42: ("Yi/Increase", "increase"),
    43: ("Guai", "breakthrough"),
    44: ("Gou", "encounter"),
    45: ("Cui", "gathering"),
    46: ("Sheng", "rising"),
    47: ("Kun/Exhaustion", "exhaustion"),
    48: ("Jing", "the well"),
    49: ("Ge", "revolution"),
    50: ("Ding", "vessel, transformation"),
    51: ("Zhen", "shock"),
    52: ("Gen", "stillness"),
    53: ("Jian/Gradual", "gradual development"),
    54: ("Gui Mei", "secondary role, imbalance"),
    55: ("Feng", "abundance"),
    56: ("Lu/Traveler", "traveler"),
    57: ("Xun", "gentle penetration"),
    58: ("Dui", "joy"),
    59: ("Huan", "dispersal"),
    60: ("Jie/Limitation", "limitation"),
    61: ("Zhong Fu", "inner truth"),
    62: ("Xiao Guo", "small excess"),
    63: ("Ji Ji", "after completion"),
    64: ("Wei Ji", "before completion"),
}


def build_hexagram_map() -> dict[tuple[int, ...], tuple[int, str, str]]:
    hexagrams = {}
    for upper_index, upper in enumerate(TRIGRAM_ORDER):
        for lower_index, lower in enumerate(TRIGRAM_ORDER):
            number = KING_WEN_TABLE[upper_index][lower_index]
            name, theme = HEXAGRAM_INFO[number]
            hexagrams[lower + upper] = (number, name, theme)
    return hexagrams


HEXAGRAMS = build_hexagram_map()


def seed_to_int(seed: str) -> int:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return int(digest[:16], 16)


def cast_line(rng: random.Random) -> tuple[int, bool, int]:
    # Three-coin method: 2=tails/yin, 3=heads/yang.
    total = sum(rng.choice([2, 3]) for _ in range(3))
    if total == 6:
        return 0, True, total
    if total == 7:
        return 1, False, total
    if total == 8:
        return 0, False, total
    return 1, True, total


def describe_hexagram(lines: tuple[int, ...]) -> dict:
    number, name, theme = HEXAGRAMS[lines]
    lower = TRIGRAMS[lines[:3]]
    upper = TRIGRAMS[lines[3:]]
    return {
        "number": number,
        "name": name,
        "theme": theme,
        "lower_trigram": {"name": lower[0], "image": lower[1]},
        "upper_trigram": {"name": upper[0], "image": upper[1]},
    }


def cast(seed: str) -> dict:
    rng = random.Random(seed_to_int(seed))
    raw_lines = [cast_line(rng) for _ in range(6)]
    lines = tuple(line for line, _changing, _total in raw_lines)
    changing = [idx + 1 for idx, (_line, is_changing, _total) in enumerate(raw_lines) if is_changing]
    changed_lines = tuple((1 - line) if is_changing else line for line, is_changing, _total in raw_lines)

    return {
        "seed_hash": hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12],
        "lines_bottom_to_top": lines,
        "coin_totals_bottom_to_top": [total for _line, _changing, total in raw_lines],
        "changing_lines": changing,
        "primary_hexagram": describe_hexagram(lines),
        "changed_hexagram": describe_hexagram(changed_lines) if changing else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Cast a deterministic I Ching hexagram.")
    parser.add_argument("--seed", required=True, help="Question or stable seed text.")
    args = parser.parse_args()
    print(json.dumps(cast(args.seed), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
