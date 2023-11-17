T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bit = list(input())
    init_bit = ["0"] * len(bit)
    count = 0
    for i in range(len(bit)):
        if bit[i] != init_bit[i]:
            init_bit[i:] = bit[i] * len(init_bit[i:])
            count += 1
    print("#{} {}" .format(test_case, count))