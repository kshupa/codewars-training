'''Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.

The binary number returned should be a string.

'''


def add_binary(a, b):
    num_sum = a + b
    num_string = format(num_sum, 'b')
    return num_string



print(add_binary(1, 1)) # == "10" (1 + 1 = 2 in decimal or 10 in binary)
print(add_binary(5, 9)) # == "1110" (5 + 9 = 14 in decimal or 1110 in binary)
