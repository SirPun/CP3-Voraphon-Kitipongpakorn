menuList = []
priceList = []
total = 0
def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],"THB")

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
for price in priceList:
    total += int(price)
print("Total :",total,"THB")
