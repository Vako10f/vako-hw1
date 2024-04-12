
#შექმენით პროგრამა, რომელსაც გადასცემთ სიას, სადაც გექნებათ მთელი რიცხვები. თქვენი დავალებაა, 
#რომ ამ სიის ორი მინიმალური რიცხვის ჯამი დააბრუნოთ: ([5, 8, 12, 18, 22]), 13), ([7, 15, 12, 18, 22]), 19),
# ([25, 42, 12, 18, 22]), 30)
list1=([5, 8, 12, 18, 22])
print(list1[0] + list1[1])
list2=([7, 15, 12, 18, 22])
print(list2[0] + list2[2])
list3=[25, 42, 12, 18, 22]
print(list3[2] + list3[4])
#შექმენით პროგრამა რომელსაც გადასცემთ მთელი რიცხვების სიას. შემდეგ უნდა მოახდინოთ გაფილტვრა:
#ახალ სიაში გადაიტანოთ მარტო ლუწი რიცხვები. ბოლოს კი დააბრუნოთ ახალი სია. test cases: [1, 2, 3, 4] -> [2, 4]
num=int(input("enter number"))
if num % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")
#3
list1=["a", "a", "b", "b"]
list2=["a", "c", "b", "d"]
if list1[0] == list2[0]:
    print(4)
elif list1[0] != list2[0]:
    print(-1)
if list1[1] == list2[1]:
    print(4)
elif list1[1] != list2[1]:
    print(-1)
if list1[2] == list2[2]:
    print(4)
elif list1[2] != list2[2]:
    print(-1)
if list1[3] == list2[3]:
    print(4)
elif list1[3] != list2[3]:
    print(-1)
sum=4-1+4-1
print(sum)

list1=["a", "a", "c", "b"]
list2=["a", "a", "b",  ""]
if list1[0] == list2[0]:
    print(4)
elif list1[0] != list2[0]:
    print(-1)
if list1[1] == list2[1]:
    print(4)
elif list1[1] != list2[1]:
    print(-1)
if list1[2] == list2[2]:
    print(4)
elif list1[2] != list2[2]:
    print(-1)
if list1[3] == list2[3]:
    print(4)
elif list1[3] != list2[3]:
    print(-1)
sum=4+4-1-1
print(sum)
list1=["a", "a", "b", "c"]
list2=["a", "a", "b", "c"]
if list1[0] == list2[0]:
    print(4)
elif list1[0] != list2[0]:
    print(-1)
if list1[1] == list2[1]:
    print(4)
elif list1[1] != list2[1]:
    print(-1)
if list1[2] == list2[2]:
    print(4)
elif list1[2] != list2[2]:
    print(-1)
if list1[3] == list2[3]:
    print(4)
elif list1[3] != list2[3]:
    print(-1)
sum=4+4+4+4
print(sum)


list1=["b", "c", "b", "a"]
list2=["",  "a", "a", "c"]
if list1[0] == list2[0]:
    print(4)
elif list1[0] != list2[0]:
    print(-1)
if list1[1] == list2[1]:
    print(4)
elif list1[1] != list2[1]:
    print(-1)
if list1[2] == list2[2]:
    print(4)
elif list1[2] != list2[2]:
    print(-1)
if list1[3] == list2[3]:
    print(4)
elif list1[3] != list2[3]:
    print(-1)
sum=-1-1-1-1
print(sum)