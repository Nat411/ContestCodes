p = input()
c = 1
s = "NO"
for i in range(1,len(p)):
  if p[i-1] == p[i]:
    c +=1
    if c >=7:
      s = "YES"
  else:
    c = 1
print(s)