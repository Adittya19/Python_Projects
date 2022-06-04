n=int(input("enter a number"))
x=len(str(n))
temp=n
sum=0
while(n>0):
      r=n%10
      sum=sum+r**x
      n=n//10
if(temp==sum):
       print("armstrong number")
else:
       print("not armstrong number")

