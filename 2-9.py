#Rule: Print every integer from 1 to 10 included and break when 5 is printed, then continue to 10.

for x in range(11):
    if x == 5:
        continue
    print(x)