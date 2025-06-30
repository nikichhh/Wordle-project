import json
import os

LOG_FILE = "data/games_log.json"


def analyze_stats():
    if not os.path.exists(LOG_FILE):
        return {
            "total_games": 0,
            "wins": 0,
            "win_rate": 0,
            "average_attempts": 0
        }

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    total_games = len(data)
    wins = sum(1 for game in data if game["guessed"])
    attempts_sum = sum(game["attempts"] for game in data if game["guessed"])
    avg_attempts = attempts_sum / wins if wins > 0 else 0
    win_rate = (wins / total_games) * 100 if total_games > 0 else 0

    return {
        "total_games": total_games,
        "wins": wins,
        "win_rate": round(win_rate, 2),
        "average_attempts": round(avg_attempts, 2)
    }
