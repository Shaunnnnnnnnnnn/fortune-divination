#!/usr/bin/env python3
"""Deterministic tarot draw utility for the fortune-divination skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import random


MAJOR = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
]

SUITS = ["Wands", "Cups", "Swords", "Pentacles"]
RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

SPREADS = {
    "single": ["Core message"],
    "three-card": ["Past/background", "Present/core", "Trend/reminder"],
    "relationship": ["Self", "Other", "Relationship field", "Obstacle", "Advice"],
    "choice": ["Option A", "Option B", "Hidden factor", "Advice"],
}


def seed_to_int(seed: str) -> int:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return int(digest[:16], 16)


def build_deck() -> list[str]:
    minors = [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]
    return MAJOR + minors


def draw(spread: str, seed: str) -> dict:
    if spread not in SPREADS:
        raise ValueError(f"Unknown spread: {spread}. Choose from: {', '.join(SPREADS)}")

    rng = random.Random(seed_to_int(f"{spread}:{seed}"))
    deck = build_deck()
    rng.shuffle(deck)

    cards = []
    for position, card in zip(SPREADS[spread], deck):
        orientation = "reversed" if rng.random() < 0.35 else "upright"
        cards.append({"position": position, "card": card, "orientation": orientation})

    return {"spread": spread, "seed_hash": hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12], "cards": cards}


def main() -> None:
    parser = argparse.ArgumentParser(description="Draw deterministic tarot cards.")
    parser.add_argument("--spread", choices=sorted(SPREADS), default="three-card")
    parser.add_argument("--seed", required=True, help="Question or stable seed text.")
    args = parser.parse_args()
    print(json.dumps(draw(args.spread, args.seed), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
