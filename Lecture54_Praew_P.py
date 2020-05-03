def login():
    user = input("Please input username:")
    password = input("Please input password:")
    if user == "Praew" and password == "Pi":
        return True
    else:
        return False

def showMenu():
    print("-----Praew Shop-----")
    print("1. one product calculator (vat include)")
    print("2. two products colculator (vat include)")
def menuSelected():
    Inputselected = int(input("Please input number:"))
    return Inputselected
def vatCalculate(totalprice):
    vat = 7/100
    total = totalprice + (totalprice * vat)
    return (total)
def priceCalculate():
    price1 = int(input("Please input price1:"))
    price2 = int(input("Please input price1:"))
    return vatCalculate(price1+price2)

if login():
    showMenu()
    if menuSelected() == 1:
         inputprice = int(input("Please input price:"))
         print(vatCalculate(inputprice))
    else:
         print(priceCalculate())
else:
    print("Not success")




'''
จะเห็นว่าแบบฝึกหัดที่เราทำมันประกอบจากหลายฟังก์ชัน
- login
- แสดงเมนู
- การตัดสินใจเลือกเมนู
- คำนวณ vat
- คำนวณ ราคาทั้งหมด 
แต่ทั้งนี้บาง function ก็สามารถรวมกันได้
เรามาเปลี่ยน ย่อยให้เป็น function กัน
user = input("Please input username:")
password = input("Please input password:")
if user == "Praew" and password == "Pi":
    print("Success")
    print("-----Praew Shop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    Inputselected = int(input("Please input number:"))
    if Inputselected == 1:
        price = int(input("input price:"))
        vat = 7 / 100
        total = price + (price * vat)
        print("Total is:", total)
    elif Inputselected == 2:
        input1 = int(input("Please input number"))
        input2 = int(input("Please input number"))
        result = input1+input2
        print("Total price:", result)
else:
    print("not success")
'''