"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730697392"


theword: str = input("Enter a 5-character word:")
if len(theword) != 5: 
    print("Error: Word must contain 5 characters") 
    exit()
character: str = input("Enter a single character:")
if len(character) != 1: 
    print("Error: Character must be a single character")
    exit()

print("Searching for " + character + " in " + theword)

   
instances: int = 0 
if str(theword[0]) == character: 
    print(character + " found at index 0 ")
    instances = instances + 1
if str(theword[1]) == character:  
    print(character + " found at index 1")
    instances = instances + 1
if str(theword[2]) == character: 
    print(character + " found at index 2")
    instances = instances + 1
if str(theword[3]) == character: 
    print(character + " found at index 3")
    instances = instances + 1
if str(theword[4]) == character: 
    print(character + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + character + " found in " + theword)
if instances == 1:
    print(str(instances) + " instance of " + character + " found in " + theword)
if instances == 2:
    print(str(instances) + " instances of " + character + " found in " + theword)
if instances == 3:
    print(str(instances) + " instances of " + character + " found in " + theword)
if instances == 4:
    print(str(instances) + " instances of " + character + " found in " + theword)
if instances == 5:
    print(str(instances) + " instances of " + character + " found in " + theword)