def main():
    import sys
    import formulas

    if len(sys.argv) <= 1:
        print("Need to provide the operator name")
        sys.exit()

    if len(sys.argv) <= 3:
        print("Need to provide at least two values")
        sys.exit()

    operator = sys.argv[1]
    values = [float(arg) for arg in sys.argv[2:]]

    if operator == 'add':
        formulas.add(values)
    elif operator == 'subtract':
        formulas.subtract(values)
    elif operator == 'divide':
        formulas.divide(values)
    elif operator == 'multiply':
        formulas.multiply(values)
    else:
        print("Valid operator names (add, subtract, multiply, divide)")
        sys.exit()


if __name__ == "__main__":
    main()
