from math import pi


def area_of_circle(diameter):
    if not isinstance(diameter, (int, float)):
        raise TypeError("The diameter must be an integer or float.")
    elif diameter <= 0:
        raise ValueError("The diameter must not be negative number.")
    else:
        radius = diameter / 2
        return pi * radius ** 2


print(area_of_circle(10))