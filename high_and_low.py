# Given a string of space separated numbers
# Return the highest  and lowest number
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    # get rid of white space
    # numbers.strip()
    # num_list = map(int, numbers.replace(" ", ",").split(","))
    num_list = [int(num) for num in numbers.replace(" ", ",").split(",")]
    min_number = str(min(num_list))
    print(min_number)
    max_number = str(max(num_list))
    print(max_number)
    numbers = "".join(max_number + min_number)

    print(numbers)


# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5")  # return "5 -3"
high_and_low("1 9 3 4 -5")  # return "9 -5"
