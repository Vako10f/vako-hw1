#1
balance=int(input("enter your balance"))
if balance >= 2500:
    print("you can buy iphone13")
else:
    print("you need more money to buy iphone13")
#2

#3
min_value = int(input("შეიყვანეთ მინიმალური მნიშვნელობა: "))
max_value = int(input("შეიყვანეთ მაქსიმალური მნიშვნელობა: "))
step = int(input("შეიყვანეთ step-ის რიცხვი: "))

for i in range(min_value, max_value + 1, step):
    print(i)     
#4
side1 = float(input("შეიყვანეთ პირველი გვერდი: "))
side2 = float(input("შეიყვანეთ მეორე გვერდი: "))
side3 = float(input("შეიყვანეთ მესამე გვერდი: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("სამკუთხედი არსებობს.")
else:
    print("სამკუთხედი არ არსებობს. შეიტანეთ გვერდები თავიდან.")
#5
min_value = int(input("შეიყვანეთ მინიმალური მნიშვნელობა: "))
max_value = int(input("შეიყვანეთ მაქსიმალური მნიშვნელობა: "))

for num in range(min_value, max_value + 1):
  if num > 1:
    sum = True
  for i in range(2, num):
    if (num % i) == 0:
      sum = False
      break
      if is_prime:
            print(num)      

#6
print("which one you want? *-+/")

number1=float(input("first number is"))
number2=float(input("second number is"))

print("select operation")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
choice= input("1/2/3/4 - ")

if choice == "1":
 print(number1+number2)
elif choice == "2":
 print(number1-number2)
elif choice == "3":
 print(number1*number2)
elif choice == "4":
 print(number1/number2)   
#7
number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print("ეს რიცხვი არის ორის ჯერადი.")
elif number % 3 == 0:
    print("ეს რიცხვი არის სამის ჯერადი.")
else:
    while True:
        number = int(input("შეყვანეთ სწორი რიცხვი: "))
        if number % 2 == 0:
            print("ეს რიცხვი არის ორის ჯერადი.")
            break
        elif number % 3 == 0:
            print("ეს რიცხვი არის სამის ჯერადი.")
            break    
#8
birth=int("enter your birthday time") 
if birth %4 == 0:
  print("ნაკიანი წელია") 
else:
  print("არ არის ნაკიანი წელი")
#9
a = float(input("შეიყვანეთ პირველი კათეტი: "))
b = float(input("შეიყვანეთ მეორე კათეტი: "))

c = (a**2 + b**2) ** 0.5
print("ჰიპოტენუზა არის:", c)       
#10
age=int(input("enter your age:"))
if age>=18:
  print("you can give your choice")
else:
  print("you cant give your choice")