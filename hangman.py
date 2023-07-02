import random
import string

_won = 0
_lost = 0


def play():
    word_list = ["python", "java", "swift", "javascript"]

    win_word = random.choice(word_list)
    guessed = []

    global _won
    global _lost

    attempts = 8

    while True:
        print(guessed)
        hidden = ''.join([i if i in guessed else i.replace(i, '-') for i in win_word])
        if hidden == win_word:
            print()
            print(f"You guessed the word {hidden}!\nYou survived!")
            _won += 1
            return
        elif attempts != 0:
            player_guess = input("Input a letter: ")
            if not player_guess or len(player_guess) > 1:
                print("Please, input a single letter.")
            elif player_guess not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif player_guess in guessed:
                print("You've already guessed this letter.")
            elif player_guess not in win_word:
                attempts -= 1
                guessed.append(player_guess)
                print("That letter doesn't appear in the word.\n")
            else:
                guessed.append(player_guess)
        else:
            print("\nYou Lost!")
            _lost += 1
            return


def main():
    print("H A N G M A N\n")

    game_exit = False

    while not game_exit:
        choice = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")

        if choice == "play":
            play()
        elif choice == "results":
            print(f"You won: {_won} times.\nYou lost: {_lost} times.")
        elif choice == "exit":
            game_exit = True
        else:
            continue


if __name__ == '__main__':
    main()
