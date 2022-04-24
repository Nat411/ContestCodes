n,m,k = map(int, input().split())
h = set(map(int, input().split()))
b = 1
for _ in range(k):
    i,l = map(int,input().split())
    if b in h:
        break
    if b == i:
        b = l  
    elif b == l:
        b = i
print(b)