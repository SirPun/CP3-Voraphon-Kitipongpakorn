usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "admin"  and passwordInput == "1234":
    print("----------------------------------")
    print("    BORNTODRINK MARKET-PLACE    ")
    print("----------------------------------")
    print("Cocoa       50 THB CHOOSE 1")
    print("Espresso    60 THB CHOOSE 2")
    print("Cappuccino  65 THB CHOOSE 3")
    print("----------------------------------")
    userSelected = int(input("CHOOSE : "))
    if userSelected == 1:
        Cocoa = 50
        Amount = int(input("Amount : "))
        print("result  = ", Cocoa * Amount, "THB.")
    elif userSelected == 2:
        Espresso = 60
        Amount = int(input("Amount : "))
        print("result  = ", Espresso * Amount, "THB.")
    elif userSelected == 3:
        Cappuccino = 65
        Amount = int(input("Amount : "))
        print("result  = ", Cappuccino * Amount, "THB.")
    else :
        print("error...")

else:
    print("wrong")
