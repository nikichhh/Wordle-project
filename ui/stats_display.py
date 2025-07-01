from tkinter import messagebox
from stats.analyzer import analyze_stats


def show_end_statistics(won, word, attempts):
    stats = analyze_stats()
    status_text = "You WON! 🎉" if won else "You LOST 😢"

    messagebox.showinfo(
        "Game Over",
        f"{status_text}\n\n"
        f"The word was: {word.upper()}\n"
        f"Your attempts: {attempts}\n\n"
        f"--- STATISTICS ---\n"
        f"Games played: {stats['total_games']}\n"
        f"Wins: {stats['wins']}\n"
        f"Win rate: {stats['win_rate']}%\n"
        f"Average attempts (wins): {stats['average_attempts']}"
    )
