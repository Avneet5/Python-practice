print("Select operation + | -| * | /")

operation = input()

print("To perfom operation a", operation, "b", "Enter values for a and b")

print("Enter a")
num1 = int(input())

print("Enter b")
num2 = int(input())

if operation == "+":
    if num1 == 56 and num2 == 9:
        print("Sum is 77.")
    elif num1 == 9 and num2 == 56:
        print("Sum is 77.")
    else:
        print("Sum is", num1+num2,".")
elif operation == "-":
    print("difference is", num1-num2,".")
elif operation == "*":
    if num1 == 45 and num2 == 3:
        print("Product is 555.")
    elif num1 == 3 and num2 == 45:
        print("Product is 555.")
    else:
        print("Product is", num1*num2,".")
else:
    if num1 == 56 and num2 == 6:
        print("Dividend is 4.")
    else:
        print("Dividend is", num1/num2,".")
