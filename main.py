import customtkinter as ctk
from words.generator import load_words, choose_random_word
from words.checker import check_guess

def main():
    current_row = [0]  # използваме списък, за да можем да го променяме в on_enter

    # Window of the game
    app = ctk.CTk()
    app.title('Wordle')
    app.geometry('600x400')
    app.resizable(True, True)

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
            for col_idx, letter in enumerate(word):
                color = ""
                if status[col_idx] == "green":
                    color = "green"
                elif status[col_idx] == "yellow":
                    color = "yellow"
                else:
                    color = "gray"

                grid_labels[row_idx][col_idx].configure(
                    text=letter.upper(),
                    fg_color=color,
                    text_color="white"
                )

            current_row[0] += 1  # отиваме на следващия ред
            if word == chosen_word:
                print("Congrats, you won!")
                # по-късно можем да добавим pop-up
            elif current_row[0] >= 6:
                print(f"You lost. The word was {chosen_word}")

        word_entry.delete(0, ctk.END)

    enter_btn = ctk.CTkButton(app, text="Enter", command=on_enter)
    enter_btn.grid(row=7, column=2, padx=10, pady=20)


    app.mainloop()

if __name__ == '__main__':
    word_list = load_words("data/dictionary.txt")
    chosen_word = choose_random_word(word_list)
    print(f"Chosen word for this game: {chosen_word}")
    main()