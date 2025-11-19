from sys import argv


def convert():
    assert len(argv) != 1
    assert int(argv[1])
    num = int(argv[1])
    if (num == 0):
        print("I'm Zero.")
    elif (num.iseven()):
        print("I'm Even.")
    else:
        print("I'm Odd.")


convert()
