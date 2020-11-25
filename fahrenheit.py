#using get and set method

class fahrenheit:
    def __init__(self,temperature = 40):
        self.temperature = temperature
        print("Given Temperature is:",self.temperature)
    def to_celsius(self):
        return(self.temperature-32)/1.8
#man = celsius(30)
#print(man.to_fahrenheit())
    def get_temperature(self):
        return self.temperature
    def set_temperature(self,value):
        if value <-273:
            raise valueerror("temperature below -273 not possible")
        self.temperature=value
        temperature = property(get_temperature,set_temperature)
c=fahrenheit()
c.temperature=40
print(c.to_celsius())
print("After converting from fahrenheit to celsius:",c.to_celsius())


