r=int(input("enter rows"))
c=int(input("enter columns"))
a=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"enter a[{i}][{j}]: "))
        t.append(val)
    a.append(t)
b=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"enter b[{i}][{j}]: "))
        t.append(val)
    b.append(t)
sum=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=a[i][j]+b[i][j]
        t.append(val)
    sum.append(t)

print(a)
print(b)
print(sum)

