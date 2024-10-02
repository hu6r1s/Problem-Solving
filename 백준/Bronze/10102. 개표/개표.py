V = int(input())
lst = list(input())

if lst.count("A") > lst.count("B"):
    print("A")
elif lst.count("A") < lst.count("B"):
    print("B")
else:
    print("Tie")