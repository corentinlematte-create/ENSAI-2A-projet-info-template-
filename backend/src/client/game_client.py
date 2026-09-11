import requests

from business_object.game import Game


def get_games() -> list[Game]:
    r = requests.get("https://0.0.0.0:5000/player")
    r.raise_for_status()
    json = r.json()
    return json