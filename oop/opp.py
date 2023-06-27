class Car():
    tax = 1
    car_num = 0
    def __init__(self, brand, model, founded_year, price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
        Car.car_num += 1
    def Brand(self):
        return self.brand
    # regular method
    def GetValue(self):
        return (self.price * self.tax)
    @classmethod
    def set_tax(cls):
        cls.tax = 1.5

    @classmethod
    def from_string(cls, car_string):
        brand, model, founded_year, price = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand, model, founded_year, price)
    @staticmethod
    def check_price(price):
        if price <= 1000:
            return "This car is chip!"
        else: return "This car is Expensive!"
        
car_temp = "Toyota-Cammry-1969-200"
car1 = Car("Vinfast","luxa", 2020, 1000)
car2 = Car("BMW","i8", 2014, 2000)
car3 = Car.from_string(car_temp) 

print(car1.check_price(car1.price))