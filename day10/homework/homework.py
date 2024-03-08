#homework 1
for i in range(0, 21):
    print(i)

#homework 2
num1 =int(input("please enter first number: "))
num2 =int(input("please enter second number: "))
if  num1 > num2:   
    for i in range(num2, num1):
        print(i)
elif num2>num1:
    for i in range(num1, num2):
        print(i)
else: 
    print(f"{num1}={num2}")

#homework 3
for i in range(50, 101):
    print(i)

#homework 4
for i in range(100, 49, -1):
    print(i)   

#homework 5
num=0
for i in range(0, 51):
    num=num+i
print(sum)

#homework 6
num3 =int(input("please enter positive number: "))
for i in range(0, num3):
    print(i)

#homework 7
user_age=int(input("Please enter your age: "))
new_user_age=user_age + 10
for i in range(user_age +1, new_user_age):
    print(i)
