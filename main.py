import customtkinter as ctk
from words.generator import load_words, choose_random_word
from words.checker import check_guess
from tkinter import messagebox
from ui.keyboard import VirtualKeyboard
from log.logger import save_game
from stats.analyzer import analyze_stats

def main():
    def on_enter():
        word = word_entry.get().strip().lower()
        if len(word) != 5:
            print("Word must be 5 letters.")
        elif word not in word_list:
            print("Invalid word!")
        else:
            print(f"Valid guess: {word}")
            status = check_guess(word, chosen_word)
            print(f"Status: {status}")

            # оцветяване на клетките
            row_idx = current_row[0]
            for idx, letter in enumerate(word):
                keyboard.update_key_color(letter, status[idx])
                color = ""
                if status[idx] == "green":
                    color = "#6aaa64"
                elif status[idx] == "yellow":
                    color = "#c9b458"
                else:
                    color = "#808080"

                grid_labels[row_idx][idx].configure(
                    text=letter.upper(),
                    fg_color=color,
                    text_color="#ffffff"
                )

            current_row[0] += 1  # отиваме на следващия ред
            if word == chosen_word:
                messagebox.showinfo("Wordle", f"Congrats! You guessed the word: {chosen_word}")
                save_game(chosen_word, True, current_row[0] + 1)
                app.destroy()
            elif current_row[0] >= 6:
                messagebox.showinfo("Wordle", f"You lost! The word was: {chosen_word}")
                save_game(chosen_word, False, 6)
                app.destroy()

        word_entry.delete(0, ctk.END)

    def on_letter_click(letter):
        current = word_entry.get()
        if len(current) < 5:
            word_entry.delete(0, ctk.END)
            word_entry.insert(0, current + letter.lower())

    def on_delete():
        current = word_entry.get()
        word_entry.delete(0, ctk.END)
        word_entry.insert(0, current[:-1])

    current_row = [0]  # използваме списък, за да можем да го променяме в on_enter

    # Window of the game
    app = ctk.CTk()
    app.title('Wordle')
    app.geometry('450x650')
    app.resizable(True, True)

    keyboard = VirtualKeyboard(app, on_letter_click, on_enter, on_delete)

    # Theme
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    # Main frame
    grid_labels = []
    for row in range(6):
        row_labels = []
        for col in range(5):
            lbl = ctk.CTkLabel(app, text=' ', width=50, height=50,
                               corner_radius=8, fg_color="white",
                               text_color="black", font=("Helvetica", 20),)
            lbl.grid(row=row, column=col, padx=5, pady=5)
            row_labels.append(lbl)
        grid_labels.append(row_labels)

    # Label for text input
    word_entry = ctk.CTkEntry(app, placeholder_text="Word")
    word_entry.grid(row=7, column=0, columnspan=3, padx=10, pady=20)

    # Button to submit the word
    enter_btn = ctk.CTkButton(app, text="Enter", command=on_enter)
    enter_btn.grid(row=7, column=2, padx=10, pady=20)

    app.mainloop()
    stats = analyze_stats()
    print("===== STATISTICS =====")
    print(f"Games played: {stats['total_games']}")
    print(f"Wins: {stats['wins']}")
    print(f"Win rate: {stats['win_rate']}%")
    print(f"Average attempts (wins): {stats['average_attempts']}")
    print("======================")

if __name__ == '__main__':
    word_list = load_words("data/dictionary.txt")
    chosen_word = choose_random_word(word_list)
    print(f"Chosen word for this game: {chosen_word}")
    main()