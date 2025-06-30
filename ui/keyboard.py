import customtkinter as ctk

class VirtualKeyboard:
    def __init__(self, parent, on_key_press, on_enter, on_backspace):
        self.frame = ctk.CTkFrame(parent)
        self.frame.grid(row=8, column = 0, columnspan=5, pady=10)

        self.buttons = {}
        self.key_status = {}

        rows = [
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM"
        ]

        for row_idx, row_letters in enumerate(rows):
            for col_idx, letter in enumerate(row_letters):
                btn = ctk.CTkButton(
                    self.frame,
                    text=letter,
                    width=35,
                    height=45,
                    command=lambda l=letter: on_key_press(l)
                )
                btn.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                self.buttons[letter] = btn

        enter_btn = ctk.CTkButton(
            self.frame,
            text="Enter",
            width=60,
            height=45,
            command=on_enter
        )
        enter_btn.grid(row=3, column=0, columnspan=2, padx=2, pady=2)

        backspace_btn = ctk.CTkButton(
            self.frame,
            text="Backspace",
            width=60,
            height=45,
            command=on_backspace
        )
        backspace_btn.grid(row=3, column=8, columnspan=2, padx=2, pady=2)

    def update_key_color(self, letter, color):
        letter = letter.upper()
        prev = self.key_status.get(letter, None)

        # приоритет: green > yellow > gray
        priority = {"green": 3, "yellow": 2, "gray": 1}

        if (prev is None) or (priority[color] > priority.get(prev, 0)):
            self.key_status[letter] = color
            if color == "green":
                self.buttons[letter].configure(fg_color="#6aaa64", text_color="white")  # Wordle green
            elif color == "yellow":
                self.buttons[letter].configure(fg_color="#c9b458", text_color="white")
            else:
                self.buttons[letter].configure(fg_color="#787c7e", text_color="white")