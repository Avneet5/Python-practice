print("Enter number of lines for pattern:")
lines = int(input())

print("For simple pattern enter 0 | For inverted pattern enter 1 :")
simple = int(input())
print()
if simple == 0:
    j = 1
    for i in range(lines):
        for k in range(j):
            print("*", end="")
        print()
        j=j+1
else:
    j = lines
    for i in range(lines):
        for k in range(j):
            print("*", end="")
        print()
        j=j-1