import random

choices= ["R", "S", "P"]

#R for Rock
#S for Scissors
#P for paper

#if:
    #paper wraps the rock,
    #rock smashs the scissors, or
    #scissors cuts the paper you(CPU or player) wins
#else you lose   

print("R for rock")
print("S for scissors")
print("P for paper")
print(" ")

while True:
    computer = random.choice(choices)
    player = input("Make your choice: R, S, P : ").upper()
    if player == computer:
        print("Player", player, ":", "CPU", computer)
        print("TIE!, Play Again")
        print("")
    elif player == "R":
        if computer == "P":
            print("Player", player, ":", "CPU", computer)
            print("CPU Win!")
            print("")
        else:
            print("Player", player, ":", "CPU", computer)
            print("You Win!")
            print("")
            break
    elif player == "P":
        if computer == "S":
            print("Player", player, ":", "CPU", computer)
            print("CPU Win!")
            print("")
        else:
            print("Player", player, ":", "CPU", computer)
            print("You Win!")
            print("")
            break
    elif player == "S":
        if computer == "R":
            print("Player", player, ":", "CPU", computer)
            print("CPU Win!")
            print("")
        else:
            print("Player", player, ":", "CPU", computer)
            print("You Win!")
            print("")
            break

    else:
        print("Error! Try Again.")
        print("")




