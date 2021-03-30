#for x in range len chaine/liste
#Goal: Display separately every character of a string, and display separately every element of a list.

string = str(input("Enter a string:\n"))
list = (string.split())

for x in range(len(string)):
    print(string[x])

for y in range(len(list)):
    print(list[y])