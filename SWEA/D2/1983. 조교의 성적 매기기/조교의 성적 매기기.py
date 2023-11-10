grade = {
    1: "A+",
    2: "A0",
    3: "A-",
    4: "B+",
    5: "B0",
    6: "B-",
    7: "C+",
    8: "C0",
    9: "C-",
    10: "D0"
}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    total = []
    for _ in range(n):
        score = list(map(int, input().split()))
        total.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)
    c = total[k - 1]
    total.sort(reverse=True)
    print("#{} {}".format(test_case, grade[total.index(c) // (n // 10) + 1]))