def lowestNumber():
    firstInput = int(input("\nInput 1st Number: "))
    secondInput = int(input("Input 2nd Number: "))
    thirdInput = int(input("Input 3rd Number: "))
    if firstInput < secondInput and firstInput < thirdInput:
        print(f"\nThe lowest number is {firstInput}.")
    elif secondInput < thirdInput:
        print(f"\nThe lowest number is {secondInput}.")
    elif firstInput == secondInput or firstInput == thirdInput:
        print(f"\nThe lowest number is {firstInput}.")
    else:
        print(f"\nThe lowest number is {thirdInput}.")

lowestNumber()