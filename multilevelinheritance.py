class Grandparent:
    def legacy(self):
        print("Family home")
class Parent(Grandparent):
    def house(self):
        print("Modern apartment")
class Child(Parent):
    def room(self):
        print("Gaming room")
obj = Child()
obj.legacy() 
obj.house()  
