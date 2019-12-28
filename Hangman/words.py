import random

WORDLIST = 'Hangman/wordlist.txt'

words = []


def get_random_word():
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as word_list:
        for word in word_list:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            num_words_processed += 1
            words.append(word)

    rand = random.randint(1, num_words_processed)
    curr_word = words[rand - 1]

    return curr_word
