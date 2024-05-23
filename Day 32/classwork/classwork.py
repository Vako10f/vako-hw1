def manual_index(numbers_list,search_value):
    if search_value not in numbers_list:
        return -1
    for i in range(0,len(numbers_list)):
        if search_value == numbers_list[i]:
            return i
        
        
