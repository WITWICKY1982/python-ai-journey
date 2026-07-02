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


