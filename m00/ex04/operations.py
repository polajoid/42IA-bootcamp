from sys import argv


def operation(param):
    try:
        assert len(param) <= 3, "too many arguments"
        assert len(param) >= 3, "too few arguments"
        assert param[1].isnumeric() and param[2].isnumeric(), "only integers"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

    a = int(param[1])
    b = int(param[2])

    print(f"Sum:\t\t {a + b}")
    print(f"Difference:\t {a - b}")
    print(f"Product:\t {a * b}")
    try:
        print(f"Quotient:\t {a / b}")
        print(f"Remainder:\t {a % b}")
    except ZeroDivisionError:
        print("Quotient:\t ERROR (division by zero)")
        print("Remainder\t ERROR (modulo by zero)")


operation(argv)
