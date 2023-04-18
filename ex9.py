import random

gold_number = random.randint(1,101) 
n = 0 
while True:

    guess_number = int(input("enter the number : "))
    n+=1
    if guess_number  < gold_number:
        print(" you choice lower number \n")
    elif guess_number == gold_number:
        print(f"you win , and you guessed this number in {n} times  ")
        break
    else:
        print("you choice higher number \n ")
        