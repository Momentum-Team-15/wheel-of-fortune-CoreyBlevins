import random   

def create_board(word):
    board_list = []
    for letter in word:
        board_list.append("_")
    print(f"\nYour {len(word)} letter word to guess is: {' '.join(board_list)}")
    print("You have 8 guesses.")
    return board_list


def show_board(word, board, correct_list):
    for letter in correct_list:
        for idx in range(len(word)):
            if word[idx] == letter:
                board[idx] = letter
    print(" ".join(board))


def get_user_guess():
    guess = input("\nGuess your letter: ")
    if len(guess) > 1:
        print("\nPlease guess only one letter.")
        guess = input("\nGuess your letter: ")
        return guess
    else:
        return guess


def play_again():
    answer = input("\nPlay again? y / n : ")
    if answer == "y":
        play_game()
    elif answer == "n":
        exit()
    else:
        print("\nPlease choose y or n.")
        play_again()


def play_game():
    with open("words.txt") as file:
        words_in_txt = file.read()
        words = words_in_txt.split()
    word_to_guess = random.choice(words)
    game_board = create_board(word_to_guess)
    correct_guesses = []
    incorrect_guesses = []
    while len(incorrect_guesses) < 8 and "_" in game_board:
        new_guess = get_user_guess().lower()
        if new_guess in word_to_guess:
            correct_guesses.append(new_guess)
        else:
            incorrect_guesses.append(new_guess)
            print(f"\nIncorrect({len(incorrect_guesses)}): {' '.join(incorrect_guesses)},")
        show_board(word_to_guess, game_board, correct_guesses)
    if len(incorrect_guesses) == 8:
        print(f"All 8 guesses used. Correct answer: {word_to_guess}")
        play_again()
    elif "_" not in game_board:
        print("Good job! You guessed it!")
        play_again()


if __name__ == "__main__":
    play_game()
