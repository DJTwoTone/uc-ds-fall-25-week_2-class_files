people = [
    ("ana",  21),
    ("ben",  19),
    ("cai",  22),
]
by_age = sorted(people, key=lambda p: p[1])
print(by_age)