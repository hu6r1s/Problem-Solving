person = []
for _ in range(28):
    person.append(int(input()))
person.sort()
for i in range(1, 31):
    if i not in person:
        print(i)