#1
for i in range(1,51,5):
    print(i-1)
#2
for i in range (2,21,2):
    print(i)
#3
for i in range(5, 11):
    num = i * i
    print(f"{i} * {i} = {num}")
#4
print(input("enter number"))
def fact( n):
  if n>1:
    return n*fact(n-1)
  else:
    return 1.
n=int(input('enter the number'))
print("Factorial of ",n,"is - ", fact(n))
#5
