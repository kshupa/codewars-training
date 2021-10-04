'''Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
If there are multiple elements with the same value, remove the one with a lower index. 
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.'''


def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    else:
        result = []
        min_number = min(numbers)
        for num in numbers:
            if num != min_number:
                result.append(num)
        
        return result

        result = []
        min_number = 1
        while i < len(numbers):
            if numbers[i] <



print(remove_smallest([1,2,3,4,5]))# = [2,3,4,5]
print(remove_smallest([5,3,2,1,4]))# = [5,3,2,4]
print(remove_smallest([2,2,1,2,1]))# = [2,2,2,1]