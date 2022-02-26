print("Start guessing:")
secret_number = 9
chances = 1
guess_limit = 3
while chances <= guess_limit:
    trying = int(input("Guess: "))
    chances += 1
    if trying == secret_number:
        print("You are the winner!")
        break
else:
    print("Sorry your chances are over")



