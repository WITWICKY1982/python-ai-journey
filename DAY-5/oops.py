class Phone:
    def set_cost(self,cost):
        self.cost = cost
    def set_colour(self,colour):
        self.colour = colour
    def show_cost(self):
        return self.cost
    def show_colour(self):
        return self.colour

p1 = Phone()
p1.set_cost("5000")
p1.set_colour("ORANGE")
p1.show_cost()
p1.show_colour()

class car:
    def __init__(self,cost,year):
        self.cost = cost
        self.year = year
    def show_car_details(self):
        print("CAR COST IS",self.cost)
        print("CAR YEAR",self.year)
c1 = car("2000000",2026)
c1.show_car_details()

class vehicle(car):
    def show_vehicledetails(self):
        print("VEHICLE PRICE",self.cost)
        print("VEHICLE YEAR",self.year)
    
v1 = vehicle(1200000,2109)
v1.show_vehicledetails()
v1.show_car_details()


class parent1:
    def set_str1(self,str1):
        self.str1 = str1
    def show_str1(self):
        return self.str1
 


class parent1:
    def set_str1(self,str1):
        self.str1 = str1
    def show_str1(self):
        return self.str1


class parent2:
    def set_str2(self,str2):
        self.str2 = str2
    def show_str2(self):
        return self.str2
    
class child(parent1,parent2):
    def set_str3(self,str3):
        self.str3 = str3
    def show_str3(self):
        return self.str3
    
c1 = child()
c1.set_str1("I AM P1")
c1.set_str2("I AM P2")
c1.set_str3(" I AM CHILD")    
    

    









    
    
    

