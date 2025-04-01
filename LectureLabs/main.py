#incorporate the random library
import random

#choose a random number as the integar value 
#to assign to the "number" variable
number = random.randint(0,100)

#average print statement
print("Guess the magic number between 0 and 100")

#assign an initial value outside of the range of 0, 100
#in order to avoid short curcuiting the loop
guess = -1  

#begin a while loop
while guess != number:
    #set guess to whatever the input is
    guess = int(input("\nEnter your guess: "))

    print(guess)

    #if user gets the correct number, notify and end the loop
    if guess == number:
        print(f"Yes, the number is {number}")
    #otherwise, notify user in terms of above or below the number and continue the loop
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
