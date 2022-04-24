l = "qwertyuiopasdfghjkl;zxcvbnm,./"
d = input()
s = input()
n = []
if d == "R":
  for i in s:
    index = l.index(i)
    n.append(l[index-1])
elif d == "L":
  for i in s:
    index = l.index(i)
    n.append(l[index+1])
t = "".join(n)
print(t)