#1
names = ["vako", "luka", "sandro", "mate", "nika"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
#2
names = ["vako", "luka", "sandro", "mate", "nika"]

for name in names:
    print(name)
#3
total = 0
product = 1

for number in range(1, 11):
    total += number
    product *= number

print(total)
print(product)
#4
total = 0

for number in range(2, 11, 2):
    print(number)
    total += number

print(total)
#5
total= 0
product = 1

for number in range(1, 11, 2):
    print(number)
    total += number
    product *= number

print( total)
print(product)
#6
word = "goal oriented academy"

for e in word:
    print(e)
#7
goa = "goal oriented academy"

for i in range(0, len(goa), 2):
    print(goa[i])