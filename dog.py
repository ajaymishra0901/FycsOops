class Dog:
  #Class Attribute
  speies='mammal'

  #Initializer/Instance Attribute
  def __init__(self,name,age):
    self.name=name
    self.age=age

  #instane method
  def description(self):
    return"{}  is {} years old".format(self.name,self.age)

  #instane method
  def speak(self,sound):
    return"{} says {} ".format(self.name,sound)

#Instantiate the dog object
mikey=Dog("Mikey",6)

#call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff "))
