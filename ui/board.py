import customtkinter as ctk


class WordleBoard:
    def __init__(self, parent):
        self.labels = []
        for row in range(6):
            row_labels = []
            for col in range(5):
                lbl = ctk.CTkLabel(parent, width=50, height=50, text="", fg_color="white", corner_radius=5)
                lbl.grid(row=row, column=col, padx=5, pady=5)
                row_labels.append(lbl)
            self.labels.append(row_labels)

    def update_row(self, row_idx, word, status, get_color):
        for col_idx, letter in enumerate(word):
            self.labels[row_idx][col_idx].configure(
                text=letter.upper(),
                fg_color=get_color(status[col_idx]),
                text_color="white"
            )
