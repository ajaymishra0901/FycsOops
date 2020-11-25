#using get and set method

class celsius:
    def __init__(self,temperature =37):
        self.temperature = temperature
        print("Given Temperature is:",self.temperature)
    def to_fahrenheit(self):
        return(self.temperature*1.8)+32
#man = celsius(30)
#print(man.to_fahrenheit())
    def get_temperature(self):
        return self.temperature
    def set_temperature(self,value):
        if value <-273:
            raise ValueError("temperature below -273 not possible")
        self.temperature=value
        temperature = property(get_temperature,set_temperature)
c=celsius()
c.temperature=37
print(c.to_fahrenheit())
print("After converting from celsius to fahrenheit:",c.to_fahrenheit())

