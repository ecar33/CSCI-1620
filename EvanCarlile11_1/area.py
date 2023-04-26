import math


def check_if_numeric(*args):
    for arg in args:
        try:
            float(arg)
            return True
        except ValueError:
            raise

def rectangle(length, width):
    if check_if_numeric(length, width):
        if float(length) < 1 or float(width) < 1:
            raise TypeError
        else:
            length = float(length)
            width = float(width)
            return length * width


def square(side):
    if check_if_numeric(side):
        if float(side) < 1:
            raise TypeError
        else:
            side = float(side)
            return side * side


def circle(radius):
    if check_if_numeric(radius):
        if float(radius) < 1:
            raise TypeError
        else:
            radius = float(radius)
            return (radius * radius) * math.pi


def triangle(base, height):
    if check_if_numeric(base, height):
        if float(base) < 1 or float(height) < 1:
            raise TypeError
        else:
            base = float(base)
            height = float(height)
            return 0.5 * base * height
