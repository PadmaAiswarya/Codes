class Animal:
    def breathe(self):
        print("Breathing...")
class Dog(Animal):
    def bark(self):
        print("Woof!")
class Cat(Animal):
    def meow(self):
        print("Meow!")
d = Dog()
c = Cat()
d.breathe()
c.breathe()
