kata = "The right format"
template = "{:>42}".format(kata)
print(template.replace(" ", "-"), end="")
