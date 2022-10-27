"""Hangaman Game"""

import random
def main():
    global name
    global random_word
    global already_guessed
    global count
    global length
    global display
    already_guessed = []
    count = 0
    print("enter your name:")
    name = input()
    print("Best of Luck "+name+"!..")
    words_list = ["python", "html", "css", "javascript", "django", "march", "growth", "ai"]
    random_word = words_list[random.randrange(0, len(words_list))]
    length = len(random_word)
    print(random_word)
    display = "_"*len(random_word)
    game()


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or play_game == "Y":
        main()
    elif play_game == "n" or play_game == "N":
        print("Thanks For Playing! We expect you back again!")
        exit()


def game():
    global random_word
    global count
    global length
    global display
    limit = 5

    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        game()
    else:
        guess = guess.lower()

    if guess in random_word:
        already_guessed.extend([guess])
        index = random_word.find(guess)
        random_word = random_word[:index] + "_" + random_word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        # print(random_word+"\n")
        # print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter...\n")

    else:
        count += 1
        # print(count)
        if count != limit:
            print("Sorry guessed letter not in word,you have "+str(limit-count)+" chances left..")
        else:
            print("Wrong guess. You lost the game!!!\n")
            print("The word was:", random_word)
            play_loop()

    if random_word == "_"*length:
        print("congrats! you did it..")
        play_loop()

    elif count != limit:
        game()


main()
