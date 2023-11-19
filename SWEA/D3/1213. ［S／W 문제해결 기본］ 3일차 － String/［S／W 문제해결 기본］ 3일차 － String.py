T = 10
for test_case in range(1, T+1):
    _ = int(input())
    sub_string = input()

    print("#{} {}".format(test_case, input().count(sub_string)))