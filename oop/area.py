def area_of_rectangle(length, width):
    if not isinstance(length, (int, float)):
        raise TypeError("Length and width must be a number")
    elif not isinstance(width, (int, float)):
        raise TypeError("Length and width must be a number")
    elif length <= 0 or width <= 0:
        raise ValueError("Length and width must not be negative number.")
    else:
        return length * width


print(area_of_rectangle(5, "0"))
