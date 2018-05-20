Calculator = True

while Calculator:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    ans = int(input("Enter Your Choice From 1-5"))

    if ans == 1:
        print("Addition")
        First = int(input("Enter First Number"))
        Second = int(input("Enter Second Number"))

        Result = First + Second
        print(First, '+', Second, '=', Result)

    elif ans == 2:
        print("Subtraction")
        First = int(input("Enter First Number"))
        Second = int(input("Enter Second Number"))

        Result = First - Second
        print(First, '-', Second, '=', Result)


    elif ans == 3:
        print("Multiplication")
        First = int(input("Enter First Number"))
        Second = int(input("Enter Second Number"))

        Result = First * Second
        print(First, '*', Second, '=', Result)


    elif ans == 4:
        print("Division")
        First = int(input("Enter First Number"))
        Second = int(input("Enter Second Number"))

        Result = First / Second
        print(First, '/', Second, '=', Result)


    elif ans == 5:
        print("OK BYEE")
        Calculator = False
