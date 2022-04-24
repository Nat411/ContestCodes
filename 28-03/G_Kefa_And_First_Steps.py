n = int(input())
a = list(map(int,input().split()))
m = []
c = 1
for i in range(0,n-1):
    if a[i] <= a[i+1]:
        c +=1
    elif a[i] > a[i+1]:
        m.append(c)
        c= 1
m.append(c)  
print(max(m))