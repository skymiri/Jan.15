""""
ACIT2515 Lab

Week 2 -- complete this file!

"""
import random

# The number of turns allowed is a global constant
NB_TURNS = 10


def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    with open("hangman/words.txt.webloc", "r") as f:
        words = f.read().split()
        chosen_word = random.choice(words).upper()
        print("Chosen word:", chosen_word)  # Debugging line
        return chosen_word


def reveal_letters(word, letters):
    word = word.upper()
    letters = [letter.upper() for letter in letters]
    return ' '.join([letter if letter in letters else '_' for letter in word])


def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    return set(word).issubset(set(letters))


def main(turns):

    word_to_guess = pick_random_word()
    letters_tried = set()
    won = False

    for _ in range(turns):
        print("Word:", reveal_letters(word_to_guess, letters_tried))

        guess = input("Guess a letter: ").upper()
        if guess in letters_tried:
            print("You already tried that letter.")
            continue

        letters_tried.add(guess)

        if all_letters_found(word_to_guess, letters_tried):
            won = True
            break

    if won:
        print("Congratulations! You've guessed the word:", word_to_guess)
    else:
        print("Out of tries! The word was:", word_to_guess)


if __name__ == "__main__":
    main(NB_TURNS)
