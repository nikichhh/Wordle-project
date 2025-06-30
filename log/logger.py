import json
from datetime import datetime
import os

LOG_FILE = "data/games_log.json"

def save_game(word, guessed, attempts):
    game_data = {
        "word": word,
        "guessed": guessed,
        "attempts": attempts,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(game_data)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
