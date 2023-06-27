class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @property
    def fullname(self):
        return f'{self.brand} {self.model}'
    @fullname.setter
    def fullname(self, full_name):
        brand, model = full_name.split(' ')
        self.brand = brand
        self.model = model
    @fullname.deleter
    def fullname(self):
        self.brand = None
        self.model = None
        print("Deleted fullname")
car = Car("Vinfast", "Luxa")
print(car.fullname)
car.fullname = "BMW i320"
print(car.brand)
del car.fullname
print(car.brand,car.model)