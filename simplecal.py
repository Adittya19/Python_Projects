def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
condition=int(input("enter the choice: "))
x=int(input("enter the number: "))
y=int(input("enter the number: "))
if condition==1:
    print("The answer is", add(x,y))
elif condition==2:
    print("The answer is", subtract(x,y))
elif condition==3:
    print("The answer is", multiply(x,y))
elif condition==4:
    print("The answer is", divide(x,y))
else:
    print("invalid output")