n=int(int(input("Enter:")))
ev=[]
while(n>0):
  rem=n%10
  if(rem%2==0):
    ev.append(rem)
  n//=10
print(ev[1])
