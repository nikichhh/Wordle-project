import random

def load_words(file_path):
    with open(file_path, "r") as f:
        words = [line.strip().lower() for line in f if len(line.strip()) == 5]
    return words

def choose_random_word(word_list):
    return random.choice(word_list)