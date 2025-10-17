"""
학생 n명을 뽑아서 1이상 스위치 개수 이하의 자연수를 나누어줌
남학생 -> if 스위치 번호가 자기가 받은 수의 배수 스위치 상태 토글
여학샘 -> 자기가 받은 수와 같은 번호의 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치의 구간을 찾아서 모두 상태 변경
1 2 3 4 5 6 7 8
0 1 0 1 0 0 0 1
man -> 0 1 1 1 0 1 0 1

"""
switch = int(input())
switch_status = [-1] + list(map(int, input().split()))
student = int(input())
for _ in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(1, switch // num + 1):
            idx = i * num
            if switch_status[idx]:
                switch_status[idx] = 0
            else:
                switch_status[idx] = 1
    else:
        left, right = num - 1, num + 1
        while (left > 0 and right <= switch) and switch_status[left] == switch_status[right]:
            left -= 1
            right += 1
        for i in range(left+1, right):
            if switch_status[i]:
                switch_status[i] = 0
            else:
                switch_status[i] = 1

for i in range(0, switch, 20):
    print(" ".join(map(str, switch_status[i+1:i+21])))