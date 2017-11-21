# Paste your code into this box
is_correct = False
low = 0
high = 100

print("Please think of a number between 0 and 100!")
while not is_correct:
    guess = int((high + low) / 2)
    print("Is your secret number " + str(guess) + "?")
    test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    valid = ['h','l','c']

    while test not in valid:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if test == 'h':
        high = guess
    elif test == 'l':
        low = guess
    else:
        print('Game over. Your seceret number was:', guess)
        is_correct = True
