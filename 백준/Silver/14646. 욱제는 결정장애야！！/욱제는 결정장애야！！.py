# n 크기 만큼 배열 2개 생성: li, check -> 하나는 돌림판, 하나는 확인용 배열
# for문 돌면서 i - 1 인덱스에 간 적 없으면 check하고 스티커 +1
# 간적 있다면 스티커 -1하고, 배열 접근 못하게 함
# 스티커에 변화가 있을 때마다 max값으로 변환
n = int(input())
li = list(map(int, input().split()))
check = [False] * (2 * n)
sticky = 0
max_sticky = 0

for i in range(2 * n):
    if not check[li[i] - 1]:
        sticky += 1
        check[li[i] - 1] = True
    else:
        sticky -= 1
    max_sticky = max(max_sticky, sticky)
print(max_sticky)