import random
print("\nrules:\n      a random number is picked\n      you can pick 1 number each time\n      you will know if the number is bigger or smaller than the number you guessed\n      you will guess till you get the correct number or you guess 10 times and lose\n      ")
guesses_left = 10
possibilities = int(input("possible numbers: "))
number = random.randint(1,possibilities)
guess = int(input("guess: "))
while guess != number:
    guesses_left -= 1
    if guesses_left == 0:
        print("you lose")
        
        break    
    elif guess > number:
        print("the number is smaller")
    elif guess < number:
        print("the number is bigger")
    guess = int(input("guess again: "))
    
    
if guesses_left != 0:
    print("thats the right number")
