def checkpassword(s):
  if(len(s)<4):
    return 0
  if(" " in s or "/" in s):
    return 0
  if(ord(s[0])>=48 and ord(s[0])<=59):
    return 0
  capital=0
  number=0
  for i in s:
    if(ord(i)>=65 and ord(i)<=90):
      capital+=1
    elif(ord(i)>=48 and ord(i)<=57):
      number+=1
  if (number>0 and capital>0):
    return 1
  return 0
s=input()
print(checkpassword(s))
