import custom_math as math

pi = 3.14


def area_circle(pi, radius):
    return math.multiplication(pi, radius**2)


def area_triangle(base, height):
    return math.multiplication(base, height) / 2


def area_rectangle(width, height):
    return math.multiplication(width, height)