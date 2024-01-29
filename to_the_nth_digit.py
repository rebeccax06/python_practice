import math

pi = math.pi
e = math.e

def nth_digit(choice, digits):
    if choice == "pi":
        return str(pi)[:digits+1]
    else:
        return str(e)[:digits+1]

def again():
    userInput = input("Do you want to find to the nth digit of pi or e? (pi/e): ").lower()
    while userInput != "pi" and userInput != "e":
        userInput = input("Please enter pi or e: ")

    digits = input("How many digits do you want to find? (Max 30): ")

    while not digits.isdigit() or int(digits) > 30 or int(digits) <0:
        digits = input("Please enter a number between 1 and 30: ")
    
    return nth_digit(userInput, int(digits))   

print(again())
user_again = input("Do you want to go again? ").lower()
while user_again == "yes":
    print(again())
    user_again = input("Do you want to go again? ").lower()

print("Thanks for coming!")


