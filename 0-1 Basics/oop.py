class Car:
     total_car =0
     def __init__(self, brand, model) -> None:
          self.__brand = brand
          self.__model = model
          Car.total_car += 1

     def get_brand(self):
           return self.__brand
     @property
     def model(self):
        return self.__model
     
     def details(self):
          print(f"you selected {self.__brand} best model {self.__model}")

     def fuel(self):     
          return "diesel or Petrol" 
      
class ElectricCar(Car):
        def __init__(self, brand, model,battery_size) -> None:
              super().__init__(brand, model)
              self.battery_size = battery_size
        
        @staticmethod
        def describe():
             return "hello car chainer"
        
        def fuel(self):     
          return "battery charge "





# my_tesla = ElectricCar("tesla","Model que", "90KWh")
# print(my_tesla.fuel())
print(ElectricCar.describe())
# my_tesla.details()
my_car = Car("tata","nano")
# my_car.model = "close"
my_car.details()
print(my_car.model)
print(my_car.fuel())
print(Car.total_car)