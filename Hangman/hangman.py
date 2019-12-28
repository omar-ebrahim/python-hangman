import string
from words import get_random_word  # words.py is a library, so it's an import

random_word = get_random_word()
max_attempts = len(random_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
incorrect_guesses = 0
correct_letters = 0


def generate_placeholder_word():
    i = 0
    temp_word = ""
    while i < max_attempts:
        temp_word += "*"
        i += 1
    return temp_word


placeholder_word = generate_placeholder_word()

game_over = False
won_game = False

print("Your word is " + str(max_attempts) +
      " letters long. You have " + str(max_attempts) + " attempts!")
print(placeholder_word)

while game_over == False:
    guessed_letter = input("Enter a letter: ")

    # entered more than 1 char
    if len(guessed_letter) > 1:
        guessed_letter = guessed_letter[0:1]
        print("You entered more than one letter. Taking first letter: " + guessed_letter)
    
    # entered nothing or just spaces
    if guessed_letter  == "" or guessed_letter.strip() == "":
        continue

    # first char isn't a letter
    if guessed_letter not in alphabet:
        print("Not a letter!")
        continue

    j = 0
    guessed_correct = False
    for char in random_word:
        # loop through characters
        if char == guessed_letter:
            # replace whatever characters in the placeholder text need replacing
            correct_letters += 1
            split_placeholder_word = list(placeholder_word)
            split_placeholder_word[j] = guessed_letter
            placeholder_word = "".join(split_placeholder_word)
            guessed_correct = True
        j += 1

    if guessed_correct:
        print("Correct! It has a " + guessed_letter + " in it!")
        print(placeholder_word)
        if correct_letters == len(placeholder_word):
            game_over = True
            print("You win!")
    else:
        print("Nope :( That's incorrect!")
        incorrect_guesses += 1
        print("You have " + str(max_attempts -
                                incorrect_guesses) + " guesses left.")
        print(placeholder_word)
        if incorrect_guesses == max_attempts:
            game_over = True
            print("You lose!")
