T = int(input())
y_point = k_point = 0

for _ in range(T):
    for _ in range(9):
        y, k = map(int, input().split())

        y_point += y
        k_point += k

    if y_point > k_point:
        print("Yonsei")
    elif y_point < k_point:
        print("Korea")
    else:
        print("Draw")