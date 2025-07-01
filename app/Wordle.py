import customtkinter as ctk

from words.generator import load_words, choose_random_word
from words.checker import check_guess
from words.coloring import get_color

from ui.keyboard import VirtualKeyboard
from ui.board import WordleBoard
from ui.stats_display import show_end_statistics

from stats.collector import collect_additional_stats
from log.logger import save_game


class Wordle:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Wordle")
        self.app.geometry("450x650")
        self.app.resizable(False, False)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # зареждаме думи
        self.word_list = load_words("data/dictionary.txt")
        self.chosen_word = choose_random_word(self.word_list)
        print(f"Chosen word for this game: {self.chosen_word}")

        # борд
        self.board = WordleBoard(self.app)

        # текущ ред
        self.current_row = 0

        self.current_guess = []

        # виртуална клавиатура
        self.keyboard = VirtualKeyboard(
            self.app,
            self.on_letter_click,
            self.on_enter,
            self.on_delete
        )

    def on_enter(self):
        word = "".join(self.current_guess)
        if len(word) != 5:
            print("Word must be 5 letters.")
        elif word not in self.word_list:
            print("Invalid word!")
        else:
            status = check_guess(word, self.chosen_word)
            print(f"Status: {status}")

            self.board.update_row(self.current_row, word, status, get_color)

            for idx, letter in enumerate(word):
                self.keyboard.update_key_color(letter, status[idx])

            self.current_row += 1

            if word == self.chosen_word:
                save_game(self.chosen_word, True, self.current_row)
                show_end_statistics(True, self.chosen_word, self.current_row)
                self.app.destroy()
            elif self.current_row >= 6:
                save_game(self.chosen_word, False, 6)
                show_end_statistics(False, self.chosen_word, 6)
                self.app.destroy()

        self.current_guess = []

    def on_letter_click(self, letter):
        if len(self.current_guess) < 5:
            self.current_guess.append(letter.lower())
            col_idx = len(self.current_guess) - 1
            self.board.labels[self.current_row][col_idx].configure(text=letter.upper())

    def on_delete(self):
        if self.current_guess:
            col_idx = len(self.current_guess) - 1
            self.board.labels[self.current_row][col_idx].configure(text=" ")
            self.current_guess.pop()

    def run(self):
        self.app.mainloop()