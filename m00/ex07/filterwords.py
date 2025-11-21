from sys import argv


def w_filter(param):
    try:
        assert len(param) == 3
        assert param[2].isnumeric()
    except AssertionError:
        print("ERROR")
        exit(1)
    S = str(param[1])
    N = int(param[2])
    S = "".join(char for char in S if char.isalnum() or char.isspace())
    print([word for word in S.split() if (len(word) > N)])


w_filter(argv)
