n, k = map(int, input().split(" "))
p = list(map(int, input().split()))
num = p[k-1]
c = 0
for i in p:
  if i >= num and i>=1:
    c+=1
  else:
    break
    
print(c)