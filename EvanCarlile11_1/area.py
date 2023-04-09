import math


def rectangle(length, width):
    if float(length) < 0 or float(width) < 0:
        raise TypeError
    else:
        length = float(length)
        width = float(width)
        return length * width


def square(side):
    if float(side) < 0:
        raise TypeError
    else:
        side = float(side)
        return side * side


def circle(radius):
    if float(radius) < 0:
        raise TypeError
    else:
        radius = float(radius)
        return (radius * radius) * math.pi


def triangle(base, height):
    if float(base) < 0 or float(height) < 0:
        raise TypeError
    else:
        base = float(base)
        height = float(height)
        return 0.5 * base * height
