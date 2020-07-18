people = ['a', 'b', 'c']

for person in people:
    print(person)

for person in people:
    if person == 'b':
        break
    print(person)


for person in people:
    if person == 'b':
        continue
    print(person)

for i in range(len(people)):
    print(i)