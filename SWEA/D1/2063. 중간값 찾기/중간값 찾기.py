T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
s = list(map(int, input().split()))
s.sort()
print(s[T // 2])