T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dict1 = {
	"01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}

for test_case in range(1, T + 1):
    s = input()
    y = s[:4]
    m = s[4:6]
    d = s[6:]
    if (int(m) < 1 or int(m) > 12) or (int(d) < 1 or int(d) > dict1[m]):
        print("#{} {}" .format(test_case, -1))
    else:
        print("#{} {}/{}/{}".format(test_case, y, m, d))