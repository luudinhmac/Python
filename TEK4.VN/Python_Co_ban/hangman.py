# Doan chu
print("Start the game...")
words = 'secret'
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in words:
        if char in guesses:
            print(char,end='')
        else:
            print("_",end ='')
            failed += 1
    if failed == 0:
        print("You Won")
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in words:
        turns -=1
        print("wrong guess")
        print("You have ", turns, "more guesses")
        if turns == 0:
            print("You lose")