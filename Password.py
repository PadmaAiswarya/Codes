s=input()
capital=0
small=0
numbers=0
special=0
for char in s:
  if(ord(char)>=65 and ord(char)<=90):
    capital+=1
  elif(ord(char)>=97 and ord(char)<=122):
    small+=1
  elif(ord(char)>=48 and ord(char)<=57):
    numbers+=1
  else:
    special+=1
print(capital,small,numbers,special)
if(len(s)==0):
  print("Please enter a password:")
else:
  if(len(s)>=8 and capital>0 and small>0 and numbers>0 and special>0):
    print("Strong password")
  else:
    print("Weak password")
