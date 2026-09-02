def linear_search(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i # Return the index of the target element
    return -1 # Return -1 if the target element is not found

numbers = [23,4,1,5]
target = 1

result = linear_search(numbers, target)
print("Number found at index : ", result) if result != -1 else print("Number not found")