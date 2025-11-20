from sys import argv


def operation(param):
    assert param[1].isnumeric() and param[2].isnumeric(), "only integers"

    a = int(param[1])
    b = int(param[2])

    print(f"Sum:\t\t {a + b}")
    print(f"Difference:\t {a - b}")
    print(f"Product:\t {a * b}")
    try:
        print(f"Quotient:\t {a / b}")
        print(f"Remainder:\t {a % b}")
    except ZeroDivisionError:
        print("ERROR (division by zero)")
        print("ERROR (remainer by zero)")


if (len(argv) == 3):
    operation(argv)
