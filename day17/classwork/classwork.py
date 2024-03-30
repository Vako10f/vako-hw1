#1
name_surname=input("enter your name and surname")
for i in range(0,len(name_surname)):
    print(name_surname[1])
#2
firstname = "Giorgi"

for i in range(0, len(firstname), 2):
    print(firstname[i])
#3
numbers=["1","2","3","4","5"]
if numbers == 4:
    print("there is")
#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jami = 0
for n in numbers:
    if n % 2 == 0:
        jami += n

print("ლუწი რიცხვების ჯამი:",jami)