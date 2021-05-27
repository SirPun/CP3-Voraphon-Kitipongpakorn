amount = int(input("amount : "))
for x in range (amount):
    amount -= 1
    print(" "*(amount)+"*"*(x+1)+"*"*(x))
