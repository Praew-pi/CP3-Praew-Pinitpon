username =input("Username:")
password =input("Password:")
if username == "Praew" and password == "Pi":
    print("---Welcome to Praew's Shop---")
    print("Our fruit")
    print("1. Orange  x1: 50 THB")
    print("2. Apple   x1: 60 THB")
    print("2. Mango   x1: 40 THB")
    userselected1 = int(input("Please select number of fruit:"))
    if userselected1 > 3:
        print("Invalid data")
    else:
        fruitnum = int(input("Number of fruit:"))
        if userselected1 == 1:
            sum = 50 * fruitnum
            print("Total:", sum)
        elif userselected1 == 2:
            sum = 60 * fruitnum
            print("Total:", sum)
        elif userselected1 == 3:
            sum = 40 * fruitnum
            print("Total:", sum)
else:
    print("Username or Password is not valid")