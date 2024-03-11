user_input=int(input("enter number: "))
factorial=1
for i in range (1,user_input+1):
    factorial*=i
print (f"factorial for {user_input} is {factorial} or {user_input}! is {factorial}")