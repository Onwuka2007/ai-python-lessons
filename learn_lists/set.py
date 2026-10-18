students = [
    {"name": "Hermoine", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Slytheriin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# ---- Using set() ----

houses = set()

# ensures no duplicates
for student in students:
    if student['house'] not in houses:
        houses.add(student['house'])

for house in sorted(houses):
    print(house)

# ---- using filter -----
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gry in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gry["name"])

# # ---- list comprehensions ----
# g = [student["name"] for student in students]
# print(*g)
