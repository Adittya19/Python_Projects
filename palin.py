a=input("enter a string: ")
output=''
i=len(a)-1
while i>=0:
    output=output+a[i]
    i=i-1
print(output)
if(a==output):
    print("palindrome")
else:
    print("not a palindrome")

