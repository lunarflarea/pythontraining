#Goal: User enters an integer, it's being filtered and only accepted if it's between 1 and 10 (1 and 10 included).

number = int(input("Enter an integer:\n"))

if number < 1 or number > 10:
    number = str(number)
    print(number + " isn't between 1 and 10, therefore it is not accepted.")
    quit
else:
    number = str(number)
    print(number + " is between 1 and 10, the input is correct.")