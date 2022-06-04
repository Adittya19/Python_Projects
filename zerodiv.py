a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
try:
    c=a/b
    print("Quotient:",c)
except ZeroDivisionError:
    print("Division by Zero!")

