class Animal:
    name = 'Hippo'
    color = 'Red'
    
    def speak(self):
        print(self.name, 'loves chocolate')

    @property
    def get_name(self):
        return self.name
    @property
    def get_color(self):
        return self.color

class Tiger(Animal): #inherited
    name = 'Tigris'

animal = Animal()
animal.speak()
tiger = Tiger()
tiger.speak()
print(f"Tiger's name is {tiger.get_name} and his color is {tiger.get_color}")
