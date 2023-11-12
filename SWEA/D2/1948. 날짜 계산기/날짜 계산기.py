T = int(input())

calender=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_cal = [0]
for i in range(len(calender)):
		sum_cal.append(sum_cal[i] + calender[i])
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    if m2 - m1 == 0:
        result = d2 - d1 + 1
    else:
        result = sum_cal[m2-1] - sum_cal[m1-1] - d1 + d2 + 1
    print("#{} {}".format(test_case, result))