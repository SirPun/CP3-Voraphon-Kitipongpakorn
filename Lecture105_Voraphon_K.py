class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirconditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello world")

class Van(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirconditioner()

van1 = Van()
van1.turnOnAirconditioner()

pickup1 = Pickup()
pickup1.turnOnAirconditioner()

estatecar1 = Estatecar()
estatecar1.turnOnAirconditioner()
