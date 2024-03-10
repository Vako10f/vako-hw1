print("which one you want? euro to lari")
print("euro to dollar")
print("dollar to euro")
print("lari to euro")
print("lari to dollar")
print("dollar to lari")



print("select operation")
print("1. euro to lari")
print("2. euro to dollar")
print("3. dollar to euro")
print("4. lari to euro")
print("5. lari to dollar")
print("6. dollar to lari")
choice= input("1/2/3/4/5/6 - ")
number = int(input("enter money quantity"))

if choice == "1":
 print(number,"*",2.90,"=",number*2.90)
elif choice == "2":
 print(number,"*",0.91,"=",number*0.91)
elif choice == "3":
 print(number,"*",1.09,"=",number*1.09)
elif choice == "4":
 print(number,"*",0.34,"=",number*0.34)
elif choice == "5":
 print(number,"*",2.66,"=",number*2.66)
elif choice == "6":
 print(number,"*", 0.38,"=",number* 0.38)
