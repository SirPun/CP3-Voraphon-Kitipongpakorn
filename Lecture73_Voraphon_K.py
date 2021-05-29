systemMenu = {"ข้าวมันไก่":45,"ข้าวหมกไก่":50,"ข้าวมันไก่ผสม":60,"ข้าวมันไก่พิเศษ":70}
menuList = []
total = 0
def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
showBill()
for i in range(len(menuList)):
    total += (int(menuList[i][1]))
print("Total =",total,"THB")
