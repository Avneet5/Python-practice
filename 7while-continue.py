while(True):
    print("Enter the number.")
    val = int(input())
    if val>100:
        print("Great!! Number is bigger than 100.")
        break
    else:
        print("Number less than or equal to 100, please enter bigger number.")
        continue
    