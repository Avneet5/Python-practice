num = 30

guess = 9

while(guess>0):
    print("Guesses left ", guess)
    yournum=int(input())
    if yournum>num:
        print()
        if guess!=1:
            print("Enter smaller number.")
    elif yournum<num:
        print()
        if guess!=1:
            print("Enter bigger number")
    else:
        print()
        print("You won!!")
        print("Guesses taken", 10-guess)
        break
    guess=guess-1
    if guess==0:
        print("Game over")
        break