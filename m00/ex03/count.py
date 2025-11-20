def text_analyzer(*arg):
    assert len(arg) <= 1, "too many arguments"
    if (len(arg) == 1):
        assert isinstance(arg[0], str), " argument is not a string"
        string = arg[0]
    elif (len(arg) == 0):
        string = input("What is the text to analyze? ")
    print(f"The text contains {len(string)} printable characters(s):")
    print(f"- {sum(1 for c in string if c.isupper())} upper letter(s)")
    print(f"- {sum(1 for c in string if c.islower())} lower letter(s)")
    print(f"- {sum(1 for c in string if c in '.,;:?!')} punctuation mark(s)")
    print(f"- {sum(1 for c in string if c in ' ')} space(s)")
