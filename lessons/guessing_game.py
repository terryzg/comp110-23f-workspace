"""Game that only completes when you guess the right number"""

from random import randint

secret: int = randint(1,10)

guess: int = int(input("Guess a number between 1 and 10: "))

number_of_tries: int = 3
tries_count: int = 0

while guess != secret and tries_count < number_of_tries:
    print("Wrong")
    if guess < 1 or guess > 10:
        print("That's not between 1 and 10")
    if guess > secret:
        print("Your guess was too high!")
    else:
        print("Your guess was too low")
    guess = int(input("Guess again: "))
    tries_count += 1
if guess == secret:
    print("You got it!")


    
#print white boxs in spots where the character is wrong and vice versa for green boxes
#while numb < 6:
   #    if guess[numb] != secret_word[numb]:
     #       print (f"{WHITE_BOX}", end="")
    #   elif guess[numb] == secret_word[numb]:
      #      print (f"{GREEN_BOX}", end="")
       #numb = numb + 1
