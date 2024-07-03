price = []
n = int(input())
for _ in range(n):
    dice = sorted(list(map(int, input().split())))
    if len(set(dice)) == 1:
        price.append(50000+dice[0]*5000)
    elif len(set(dice)) == 2:
        if dice[1] == dice[2]:
            price.append(10000 + dice[1] * 1000)
        else:
            price.append(2000 + dice[0] * 500 + dice[2] * 500)
    elif len(set(dice)) == 3:
        for i in range(3):
            if dice[i] == dice[i+1]:
                price.append(1000+dice[i]*100)
                break
    elif len(set(dice)) == 4:
        price.append(dice[3]*100)
print(max(price))