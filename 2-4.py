#Goal: Increase a if it's lower than b, and decrease b if it's greater than 0. Print b if its value is odd.

a = int(0)
b = int(10)

while a < b:
    print(a)
    a += 1

while b > 0:
    b -= 1
    if (b % 2) != 0:
        print(b)
