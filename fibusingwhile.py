n=int(input("enter the range"))
a=0
b=1
i=0
print(a)
print(b)
while(i<(n-2)):
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1

