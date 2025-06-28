def check_guess(guess, target_word):
    """
    Връща списък със статуса на буквите:
    - 'green'  = правилно място
    - 'yellow' = грешно място, но присъства
    - 'gray'   = не присъства
    """
    result = ['gray'] * 5
    target_copy = list(target_word)

    # първо зелените
    for i in range(5):
        if guess[i] == target_word[i]:
            result[i] = 'green'
            target_copy[i] = None  # премахваме, за да не го броим втори път

    # после жълтите
    for i in range(5):
        if result[i] == 'gray' and guess[i] in target_copy:
            result[i] = 'yellow'
            target_copy[target_copy.index(guess[i])] = None

    return result