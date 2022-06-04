print("select conversion")
print("1. C to f")
print("2. f to c")
condition=int(input("select choice")) 
if condition==1:
    celsius=float(input("enter temperature in c:"))
    farhenheit= celsius*(9/5)+32
    print(farhenheit)
else:
    farhenheit=float(input("enter temperature in f:"))
    celsius= (farhenheit-32)*5/9
    print(celsius)

