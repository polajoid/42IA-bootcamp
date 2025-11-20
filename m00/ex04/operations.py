from sys import argv


def error_manager(*argv):
    # assert len(argv) == 4, "too many arguments"
    assert argv[1].isnumeric() and argv[2].isnumeric(), "only integers"

    a = int(argv[1])
    b = int(argv[2])

    print(f"Sum:\t {a + b}")
    print(f"Difference:\t {a - b}")
    print(f"Product:\t {a * b}")
    print(f"Quotient:\t {a / b}")
    print(f"Remainder:\t {a % b}")


if (len(argv) != 1):
    error_manager(argv)
