t = int(input())
for _ in range(t):
  c = 0
  l = []
  k = input()
  if len(k) == 1:
    print(1)
    print(int(k))
  else:
    for i in range(len(k)):
      if k[i] !="0":
        c += 1
        l.append(int(k[i]+"0"*(len(k)-i-1)))
    print(c)
    print(*l)