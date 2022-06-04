print("1. Addition")
print("2. subtraction")
print("3. Multiplication")
print("4. Division")
condition=int(input("select choice"))
if condition==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print(c)
elif condition==2:
        a=int(input("Enter A:"))
        b=int(input("Enter B:"))
        c=a-b
        print(c)
elif condition==3:
            a=int(input("Enter A:"))
            b=int(input("Enter B:"))
            c=a*b
            print(c)
elif condition==4:
                a=int(input("Enter A:"))
                b=int(input("Enter B:"))
                c=a/b
                print(c)
else:
                print("Invalid Choice")
    

