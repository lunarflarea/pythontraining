#Purpose: User enters a float. If it's 0 or above 0, we display the float's sqrt. Else, we print an error.

from math import sqrt

number = float(input("Enter a float\n"))

if number >= 0:
    result = sqrt(number)
    print(result)
elif number < 0:
    print("Error: Please enter a float equal or above to 0.")