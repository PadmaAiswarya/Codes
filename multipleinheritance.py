class Father:
    house = 1

class Mother:
    car = 2

class Child(Father, Mother):
    toy = 3

boy = Child()
print(boy.house)
print(boy.car)
print(boy.toy)
