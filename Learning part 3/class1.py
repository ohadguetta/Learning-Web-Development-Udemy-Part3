class Animal:
    name = 'Uranga'

    def set_name(self,name):
        self.name = name
        return name

    @property
    def get_name(self):
        return self.name

animal = Animal()
print(animal.get_name)
animal.set_name('Hippo')
print(animal.get_name)