T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    string = ""
    for i in range(n):
        c, k = input().split()
        string += c * int(k)
        
    print("#{}" .format(test_case))
    for i in range(0, len(string), 10):
        print(string[i:i+10])