n = int(input("Enter:"))
if n < 0:
    n = -n
while n != 0:
    rem = n % 10
    if rem % 2 != 0:
        print(rem)
        break
    n //= 10
else:
    print("No odd digits found")
