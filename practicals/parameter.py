class car:
    wheels = 4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def displayInfo(self):
        print(f"This {self.brand} is {self.color} color")
        self.displayInfo
        
mycar = car("Tesla","Red")
mycar.displayInfo()