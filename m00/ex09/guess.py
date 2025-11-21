from random import randint


def guess():
    i = 0
    n = randint(1, 100)
    while True:
        try:
            answer = input("What's yout guess between 1 and 99?\n")
            i += 1
            assert answer.isnumeric()
        except (EOFError, AssertionError):
            print("Wrong. Try again\n")
            continue
        if (int(answer) > n):
            print("Too High!\n")
        elif (int(answer) < n):
            print("Too Low!\n")
        else:
            print(f"Amazing! You found in {i} rounds\n")
            break


guess()
