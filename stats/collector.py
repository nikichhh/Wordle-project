def collect_additional_stats(games_data):
    # например да върне най-често срещаните думи
    freq = {}
    for game in games_data:
        word = game['word']
        freq[word] = freq.get(word, 0) + 1
    return freq