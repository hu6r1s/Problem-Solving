string = list(input())
if "".join(string) == "".join(reversed(string)):
    print(1)
else:
    print(0)