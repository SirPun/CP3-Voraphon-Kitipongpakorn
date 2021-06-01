class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to",self.name,self.lastName+"'s cart")

customer1 = Customer()
customer1.name = input("Your name : ")
customer1.lastName = input("Your lastname : ")
customer1.age = input("Your age : ")
customer1.addCart()

customer2 = Customer()
customer2.name = input("Your name : ")
customer2.lastName = input("Your lastname : ")
customer2.age = input("Your age : ")
customer2.addCart()

customer3 = Customer()
customer3.name = input("Your name : ")
customer3.lastName = input("Your lastname : ")
customer3.age = input("Your age : ")
customer3.addCart()
