#number4
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage =mileage
class Bus(Vehicle):
     def show(self,color="white"):
        self.color=color
        print("color:",self.color,"vechicle name:",self.name,"speed",self.max_speed,"mileage",self.mileage)
car1=Bus("school volvo",180,12)
car1.show()
car2=Bus("audi Q5",240,18)
car2.show() 
class Car(Vehicle):
     pass

# #number 3
class Vehicle:
   def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage =mileage
class Bus(Vehicle):
    def show(self,seating_capacity=50):
        self.seating_capacity=seating_capacity
        print("The seating capacity of a bus is",self.seating_capacity,"Passengers")
car=Bus("subaru",230,12)
car.show(seating_capacity:=50)

#number5
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage =mileage
    def fare(self,seating_capacity):
        self.seating_capacity=seating_capacity
        return self.seating_capacity *100
class Bus(Vehicle):
    def fare(self,seating_capacity):
        self.seating_capacity=seating_capacity
        amount =super().fare(seating_capacity)
        amount+=amount*10/100
        return amount
school_bus=Bus("school volvo",12,50)
print("total Bus Fare is:",school_bus.fare(seating_capacity=50))
    
#number1
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
car=Vehicle("180km/hr",90)
print(car.max_speed,car.mileage)

#number2
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def bus(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        print("Vehicle name:",self.name,self.max_speed,self.mileage)
car=Vehicle("school volvo",180)
car.bus("school volvo",180,12)




