fruits=["orange","apple","guava","banana"]
vegetables=["carrot","potato","onion","cabbage"]
numbers=[10,20,30,40]
float=[1.1,2.1,3.1,4.1]

print(fruits[0])
print(vegetables[0])
print(numbers[0])
print(float[0])
print(fruits[0:2])
print(vegetables[0:3])
print(numbers[1:])
print(float[1:])
fruits.append("strawberry")
print(fruits)
vegetables.append("springonion")
print(vegetables)
numbers.append(50)
print(numbers)
float.append(5.1)
print(float)
fruits[0]="mango"
print(fruits)
vegetables[0]="mushroom"
print(vegetables)
numbers[0]=60
print(numbers)
float[0]=6.1
print(float)
fruits.insert(0, "orange")
print(fruits)
vegetables.insert(0, "carrot")
print(vegetables)
numbers.insert(0, 10)
print(numbers)
float.insert(0, 1.1)
print(float)
del fruits[0]
print(fruits)
del fruits[2]
print(fruits)
del vegetables[0]
print(vegetables)
del numbers[0]
print(numbers)
del float[0]
print(float)
print(fruits+vegetables)