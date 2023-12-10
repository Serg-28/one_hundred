import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)
continue_game = True

attempts = word_length

display = []
for _ in range(word_length):
    display.append("_")

while continue_game:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        attempts -= 1
        print(attempts)
        if attempts < 1:
            print("You lose")
            continue_game = False

    else:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess

        if "_" not in display:
            print("You win!")
            continue_game = False

    print(display)
