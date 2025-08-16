S = input()
left_hand = "qwertyasdfgzxcvb"
right_hand = "uiophjklnm"

left_cnt, right_cnt, other_cnt = 0, 0, 0

for ch in S:
    if ch == " ":
        other_cnt += 1
    elif ch.isupper():
        lower = ch.lower()
        if lower in left_hand:
            left_cnt += 1
        elif lower in right_hand:
            right_cnt += 1
        other_cnt += 1
    else:
        if ch in left_hand:
            left_cnt += 1
        elif ch in right_hand:
            right_cnt += 1

while 0 < other_cnt:
    if left_cnt <= right_cnt:
        left_cnt += 1
    else:
        right_cnt += 1
    other_cnt -= 1

print(left_cnt, right_cnt)