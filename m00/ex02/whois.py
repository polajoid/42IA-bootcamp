from sys import argv


def convert():
    assert len(argv) == 2, "more than one argument is provided"
    assert argv[1].isnumeric(), "argument is not an integer"
    num = int(argv[1])
    if (num == 0):
        print("I'm Zero.")
    elif (num & 1):
        print("I'm Odd.")
    else:
        print("I'm Even.")


convert()
