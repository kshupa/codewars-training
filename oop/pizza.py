from math import pi


def area_of_a_circle(diameter):
    if not isinstance(diameter, (float, int)):
        raise TypeError('The diameter must be integer or float')
    elif diameter < 0:
        raise ValueError('The diameter must not be negative')
    else:
        radius = diameter / 2
        return pi * radius ** 2


def price_of_round_pizza(diameter):
    return 5.00 + 0.05 * area_of_a_circle(diameter)


def print_area_of_a_circle(diameter):
    result = print_area_of_a_circle(diameter)
    print(f'A {diameter} inch circle has an area of {result:.2f}')


def price_a_pizza(diameter):
    result = price_of_round_pizza(diameter)
    print(f'A {diameter} inch pie will cost ${result:.2f}')


def number_of_ideal_slices(diameter):
    width = round(2 * pi, 2)
    circumference = round(diameter * pi, 2)
    slices = circumference // width
    waste = circumference % width
    msg = f'A {diameter} pie can be cut into {slices:.0f} {width:.2f} slices'
    if waste > 0.5:
        msg += f' , but wastes {waste:.2f}'
    print(msg + '.')


def forEach(dataset, operation):
    for element in dataset:
        try:
            operation(element)
        except Exception as e:
            print(f'Error doing {operation.__name__} on value {element}: {e} ')


pie_sizes = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

forEach(pie_sizes, print_area_of_a_circle)
forEach(pie_sizes, number_of_ideal_slices)