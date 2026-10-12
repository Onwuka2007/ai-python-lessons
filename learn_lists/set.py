students = [
    {'name': 'Hermoine', 'house': 'Gryffindor'},
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Slytheriin'},
    {'name': 'Padma', 'house': 'Ravenclaw'},   
]

houses = set()

for student in students:
    if student['house'] not in houses:
        houses.add(student['house'])
        
for house in sorted(houses):
    print(house)