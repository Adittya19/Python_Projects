class simpcal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
       return self.a+self.b
    def sub(self):
       return self.a-self.b
    def mul(self):
       return self.a*self.b
    def div(self):
       return self.a/self.b
print("1. Addition")
print("2. Subtraction")
print("3. multiplication")
print("4. division")
a=int(input("enter a number: "))
b=int(input("enter a number: "))
obj= simpcal(a,b)
condition=int(input("enter a choice: "))
if condition==1:
    print("answer", obj.add())
elif condition==2:
    print("answer", obj.sub())
elif condition==3:
    print("answer", obj.mul())
elif condition==4:
    print("answer", obj.div())
else:
    print("invalid choice")
         

         
     
    