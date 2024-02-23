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
 