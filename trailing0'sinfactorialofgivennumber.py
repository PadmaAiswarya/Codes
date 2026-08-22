from math import *
n = int(input("Enter: "))
count = 0
if n > 1:
    f = factorial(n)
    while f > 0:
        rem = f % 10
        if rem == 0:
            count += 1
            f //= 10
        else:
            break
print(count)
