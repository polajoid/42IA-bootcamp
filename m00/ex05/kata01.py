kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

print(f"{x} was created by {kata[x]}".format(" ".join(x, kata[x] for x in kata)))
