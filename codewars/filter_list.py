'''Create a function that takes a list of non-negative integers and strings and 
returns a new list with the strings filtered out.'''


def filter_list(lst):
    '''Returns new list with strings filtered out'''
    new_list = []
    for item in lst:
        if type(item) == int:
            new_list.append(item)
    
    return new_list


print(filter_list([1, 2, 'a', 'b']))  # [1,2]
print(filter_list([1, 'a', 'b', 0, 15]))  # [1,0,15]
print(filter_list([1, 2, 'aasf', '1', '123', 123]))  # [1,2,123]
