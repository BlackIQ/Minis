import random
javab = random.randint(1,99)

hads = int(input())
while hads != javab:
    if hads > javab:
        print("smaller")
    else:
        print("bigger")
    hads = int(input())

print("thats right")