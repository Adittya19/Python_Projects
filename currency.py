print("select currency")
print("1. inr to dollar")
print("2. dollar to inr")
print("3. inr to euro")
print("4. euro to inr")
condition= int(input("Select choice"))
if condition==1:
    inr= int(input("enter amount in inr:"))
    dollar=(inr/75)
    print(dollar)
elif condition==2:
    dollar= int(input("enter amount in dollar:"))
    inr=(dollar*75)
    print(inr)
elif condition==3:
    inr= int(input("enter amount in inr:"))
    euro=(inr/100)
    print(euro)
else:
    euro=int(input("enter amount in euro:"))
    inr=(euro*100)
    print(inr)

