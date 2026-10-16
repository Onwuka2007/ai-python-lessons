def total(g, s, k, *args):
    return (g * 17 + s) * 29 + k


c = [20, 10, 40]

d = {
    "g": 100,
    "s": 40,
    "k": 60,
}

# unpack all values of lists
print(total(*c), "knuts")

# unpack all values of dicts
print(total(**d), "knuts")
