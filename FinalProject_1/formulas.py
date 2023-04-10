def add(values):
    print(f'Answer = {sum(values):.2f}')


def subtract(values):
    difference = values[0]
    for i in range(1, len(values)):
        difference -= values[i]
    print(f'Answer = {difference:.2f}')


def multiply(values):
    product = values[0]
    for i in range(1, len(values)):
        product *= values[i]
    print(f'Answer = {product:.2f}')


def divide(values):
    import sys
    quotient = values[0]
    for i in range(1, len(values)):
        if values[i] != 0:
            quotient /= values[i]
        else:
            print("Cannot divide by 0")
            sys.exit()
    print(f'Answer = {quotient:.2f}')
