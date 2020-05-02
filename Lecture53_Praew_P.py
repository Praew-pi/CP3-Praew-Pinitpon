def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
inputprice = float(input("Please input price:"))
print(vatCalculate(inputprice))