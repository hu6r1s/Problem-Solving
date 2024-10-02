A, B, C = map(int, input().split())
D = int(input())

tmp = A * 3600 + B * 60 + C + D
hour = tmp // 3600 % 24
minute = tmp // 60 % 60
second = tmp % 60

print(hour, minute, second)