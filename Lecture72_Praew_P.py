menuList = []
#priceList = []

def showBill():
    print("-----Praew Restaurant-----")
    print("Order List")
    for number in range(len(menuList)):
        print(menuList[number])

def totalPrice():
    sum = 0
    for price in range(len(menuList)):
        x = (menuList[price][1])
        sum += x
    return(sum)


while True:
    menuName = input("Please enter your menu:")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Please input price:"))
        menuList.append([menuName,menuPrice])

showBill()
print("Total price is:",totalPrice(), "Baht")

