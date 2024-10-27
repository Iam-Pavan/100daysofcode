import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




word_list = ['fgfgfg','dfdfdf','dfdfdfdf']
lives = 0
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)
# step-2
# TODO-1 - Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
# word_length = len(chosen_word)
for position in range(1,6):
    placeholder += "_"
print(placeholder)

# step-2
# TODO-2 Create a "display" that puts the guess letter in the right position and _
# TODO-3 - check if the letter the user guessed (guess) is one of the letter in the chosen_word. Print "Right" if it is, "Wrong" if it`s not.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
game_over = False
correct_letters = []

while not game_over:
    guess = input("guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives += 1
        if lives == 6:
            game_over = True
            print("you lose")

    if "_" not in display:
        game_over = True
        print("you win!")

    print(stages[lives])


