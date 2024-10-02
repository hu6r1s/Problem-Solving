string = list(input())
result = 10
for i in range(1, len(string)):
    if string[i] == string[i-1]:
        h = 5
    else:
        h = 10

    result += h
print(result)