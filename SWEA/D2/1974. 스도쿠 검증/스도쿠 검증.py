T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li = [list(map(int, input().split())) for _ in range(9)]
    li2 = list(zip(*li))
    count = 0
    for i in range(9):
        if len(set(li[i])) == 9:
            count += 1
        if len(set(li2[i])) == 9:
            count += 1
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [row[j:j+3] for row in li[i:i+3]]
            li_33 = []
            for row in subgrid:
                for num in row:
                    li_33.append(num)
            if len(set(li_33)) == 9:
                count += 1
    if count == 27:
        print("#{} {}" .format(test_case, 1))
    else:
        print("#{} {}" .format(test_case, 0))