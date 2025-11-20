def text_analyzer(string):
    assert isinstance(string, str), " argument is not a string"
    if (string == ""):
        string = input("What is the text to analyze?")
    print(f"The text contains {len(string)} printable characters(s):")
    print(f"- {sum(1 for c in string if c.isupper())} upper letter(s)")
    print(f"- {sum(1 for c in string if c.islower())} lower letter(s)")
    print(f"- {sum(1 for c in string if c in '.,;:?!')} punctuation mark(s)")
    print(f"- {sum(1 for c in string if c in ' ')} space(s)")
