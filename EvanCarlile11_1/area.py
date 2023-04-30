import math


def check_if_numeric(*args):
    for arg in args:
        try:
            float(arg)
            return True
        except ValueError:
            raise
def check_if_positive(*args):
    for arg in args:
        if float(arg) <= 0:
            raise TypeError
    return True



def rectangle(length, width):
    if check_if_numeric(length, width):
        if check_if_positive(length, width):
            length = float(length)
            width = float(width)
            return length * width


def square(side):
    if check_if_numeric(side):
        if check_if_positive(side):
            side = float(side)
            return side * side


def circle(radius):
    if check_if_numeric(radius):
        if check_if_positive(radius):
            radius = float(radius)
            return (radius * radius) * math.pi


def triangle(base, height):
    if check_if_numeric(base, height):
        if check_if_positive(base, height):
            base = float(base)
            height = float(height)
            return 0.5 * base * height
