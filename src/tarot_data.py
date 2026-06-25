import json
import random
import requests

TAROT_URL = "https://raw.githubusercontent.com/smallcat419/tarot-card-data/main/index.json"


def fetch_tarot_cards():
    resp = requests.get(TAROT_URL, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data["cards"]


def pick_card_of_the_day(cards):
    card = random.choice(cards)
    is_reversed = random.choice([True, False])
    orientation = "reversed" if is_reversed else "upright"
    return {
        "name": card["name"],
        "arcana": card.get("arcana", "Minor"),
        "suit": card.get("suit", ""),
        "keywords": card.get("keywords", []),
        "orientation": orientation,
        "meaning": card[orientation]["meaning"],
        "love": card[orientation].get("love", ""),
        "career": card[orientation].get("career", ""),
        "yes_no": card.get("yes_no", ""),
        "element": card.get("element", ""),
        "astrological": card.get("astrological", ""),
    }
