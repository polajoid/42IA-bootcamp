# Simple exercise : a program that reverse a string given a parameter

import sys

def reverse(*args):
    result = ""
    for i in range(1, len(sys.argv)):
        result += str(sys.argv[i])
        if (i != len(sys.argv) - 1):
            result +=  " "
    result = result.swapcase()
    print(result)

reverse(sys.argv)
