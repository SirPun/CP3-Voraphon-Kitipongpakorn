menuList = []
total = 0
def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number])

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])
for i in range(len(menuList)):
    total = total + int(menuList[i][1])
showBill()
print("total",total,"THB")
