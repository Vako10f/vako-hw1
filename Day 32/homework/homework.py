#1
def manual_index(numbers_list, search_value):
    for index, value in enumerate(numbers_list):
        if value == search_value:
            return index
    
    return -1

numbers_list = [10, 20, 30, 40, 50]
search_value = 30
result = manual_index(numbers_list, search_value)
print(f"The index of {search_value} is {result}")
#2
def manual_max(numbers_list):
    max_value = numbers_list[0]
    for number in numbers_list:
        if number > max_value:
            max_value = number
    
    return max_value


def manual_min(numbers_list):
    min_value = numbers_list[0]
    for number in numbers_list:
        if number < min_value:
            min_value = number
    
    return min_value

numbers_list = [10, 20, 30, 40, 50]

max_value = manual_max(numbers_list)
min_value = manual_min(numbers_list)

print(f"The maximum value is {max_value}")
print(f"The minimum value is {min_value}")
#3
def manual_pop(numbers_list, index):
    if index < 0 or index >= len(numbers_list):
        raise IndexError("Index out of range")
    new_list = []
    
    for i in range(len(numbers_list)):
        if i != index:
            new_list.append(numbers_list[i])
    
    return new_list

numbers_list = [10, 20, 30, 40, 50]
index_to_remove = 2
new_list = manual_pop(numbers_list, index_to_remove)
print(f"The new list is: {new_list}")