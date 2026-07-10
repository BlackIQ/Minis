import random
import time

def game(computer, range):
    javab = random.randint(range[0],range[1])
    range = [range[0],range[1]]

    print("Guess a number between", range[0], "and", range[1], ":")
    if computer.lower() == "manual":
        hads = int(input())
    else:
        guess = random.randint(range[0],range[1])
        print("I guess", guess, "from range", range[0], "to", range[1], "!")
        hads = guess
        time.sleep(3)
    while hads != javab:
        if hads > javab:
            print(">>> Smaller!")
            range = [range[0],hads]
        else:
            print(">>> Bigger!")
            range = [hads,range[1]]
        print("Guess a number between", range[0], "and", range[1], ":")

        if computer.lower() == "manual":
            hads = int(input())
        else:
            guess = random.randint(range[0], range[1])
            print("I guess", guess, "from range", range[0], "to", range[1], "!")
            hads = guess
            time.sleep(3)

    print("Thats right!")

#### MAIN ####
def simple_game():
    bad = True
    while bad == True:
        print("Type computer or manual: ")
        computer = input()
        
        if not computer.lower() == "computer" and not computer.lower() == "manual":
            print("Wrong input. Try again.")
        else:
            bad = False
    print("Type range for guessing (in format <num> to <num>):")
    range = input()
    range = range.split("to")
    range[0] = int(range[0].replace(" ",""))
    range[1] = int(range[1].replace(" ",""))

    game(computer, range)   

if __name__=="__main__": 
    simple_game() 