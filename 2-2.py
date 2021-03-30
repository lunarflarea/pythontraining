#Purpose: Compare two words entered by the user to return the first one in the alphabetical order.

word1 = str(input("Enter the first word:\n"))
word2 = str(input("Enter the second word:\n"))

if word1 != word2:
    pass
elif word1 == word2:
    print("Error: Enter two different words")
    quit()

list = [word1, word2]

answer = min(x for x in list if isinstance(x, str))
print("The first word is " + answer)