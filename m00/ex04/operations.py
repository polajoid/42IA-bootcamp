from sys import argv

def operation(param):
    assert param[1].isnumeric() and param[2].isnumeric(), "only integers"

    a = int(param[1])
    b = int(param[2])

    print(f"Sum:\t {a + b}")
    print(f"Difference:\t {a - b}")
    print(f"Product:\t {a * b}")
    print(f"Quotient:\t {a / b}")
    print(f"Remainder:\t {a % b}")


if (len(argv) == 3):
    # print(f"Len {len(argv)}, argv[0] {argv[2]}")
    operation(str(argv))
