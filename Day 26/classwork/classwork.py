#1
def numbers(start, end):
    for num in range(start, end + 1):
        print(num)

start = 4
end = 9
print("Numbers between", start, "and", end, "are:")
numbers(start, end)
#2
def numbers1(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


start = 2
end = 6
print( start, end, numbers1(start, end))


#3
def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)

#4
def nameindex(name, index):
    if index >= 0 and index < len(name):
        print(index,name, name[index])
    else:
        print(name)

name = "vako"
index = 2
nameindex(name, index)