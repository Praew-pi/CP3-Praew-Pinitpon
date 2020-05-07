
menuList = [] #สร้าง list ไว้สำหรับใส่ข้อมูลที่ลูกค้าใส่
priceList = []
#print(menuList, priceList) จะเห็นว่าชื่อสินค้าและราคาอยู่ใน ลำดับเดียวกัน

def showBill():
    print("-----Praew Restaurant-----")
    print("Order List")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
def total(price):
    totalprice = 0
    for i in priceList:
        totalprice += i
    return totalprice

while True:
    menuName = input("Please enter your menu:")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = float(input("Please input price:"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
print("Total Price is:",total(priceList), "Baht")
