
def fact( n):
  if n>1:
    return n*fact(n-1)
  else:
    return 1.
i=int(input('enter the number'))
print("Factorial of ",i,"is - ", fact(i))

