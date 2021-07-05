import random
import words


def main():
    # set default number of lives
    lives = 6
    # list of guesses user has already made
    already_guessed = []

    # get list of words
    # choose random word
    word = random.choice(words.word_lst)
    # get length of random word
    word_length = len(word)

    display = []
    # display '_' based on length of word
    for i in range(0, word_length):  # 0 to word_length - 1
        display.append('_')

    while lives > 0:
        # Display guess word as-is
        print(f'{" ".join(display)}')

        # Display lives remaining
        print(f'You have {lives} lives left')
        draw_stick_man(lives)

        # Display guesses so far
        print(f'You have guessed these letters: {",".join(already_guessed)}')

        # ask player to guess a letter
        user_guess = input('Guess a letter: ')

        # check if player's guess match any letters in the random word
        # https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
        index = 0
        matches = []
        found_match = False
        while index < word_length:  # keep searching as long as index is still inside the word
            index = word.find(user_guess, index)  # find the next match starting at the index
            if index == -1:  # no match
                break  # stop searching
            else:
                found_match = True
                matches.append(index)
                index += 1  # search next part of the word

        if found_match:  # if correct
            # add letter at index location of displayed word list
            for i in matches:
                display[i] = user_guess
            # add letter to list of guesses
            already_guessed.append(user_guess)
        else:  # if incorrect
            print('Incorrect')
            # decrement lives
            lives -= 1
            # add letter to list of guesses
            already_guessed.append(user_guess)

        # check if joined list matched random selected word
        # use ''.join(list) to combine the list into a string
        if word == ''.join(display):  # player won
            break

    draw_stick_man(lives)
    if lives <= 0:
        print(f'You lost the hang man game. The word was {word}!')
    else:
        print(f'Congrats! You guessed the right letters to form {word}!')


def draw_stick_man(lives):
    print('-----')
    print('    |')
    if lives == 6:
        pass
    elif lives == 5:
        print('    O')
    elif lives == 4:
        print('    O')
        print('    |')
    elif lives == 3:
        print('    O')
        print('   /|')
    elif lives == 2:
        print('    O')
        print('   /|\\')
    elif lives == 1:
        print('    O')
        print('   /|\\')
        print('   / ')
    else:
        print('    O')
        print('   /|\\')
        print('   / \\')


if __name__ == "__main__":
    main()
