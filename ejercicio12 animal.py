class Animal:
    def sonido(self):
        return "el animal hace un sonido."
    

class Perro (Animal):
    def sonido (self):
        return "El perro ladra."
    

class Gato (Animal):
    def sonido(self):
        return "El gato maulla"
    

animales = [Perro(), Gato()]

for animal in animales:
    print (animal.sonido())