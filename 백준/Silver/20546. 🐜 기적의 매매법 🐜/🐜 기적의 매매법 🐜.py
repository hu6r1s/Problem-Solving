money = int(input())
stocks = list(map(int, input().split()))

def junhyeon(money, stocks):
    cnt = 0
    for stock in stocks:
        if money >= stock:
            cnt += money // stock
            money %= stock
    return money + cnt * stocks[-1]


def sungmin(money, stocks):
    """
    현금보다 주가가 비싸면 살 수 없음.
    3일 연속 가젹이 상승하면 전부 매도
    가격이 같으면 상승이 아님
    3일 연속 하락하면 전량 매수
    """
    cnt = 0
    for i in range(len(stocks) - 4):
        if stocks[i] < stocks[i+1] < stocks[i+2] < stocks[i+3]:
            money += cnt * stocks[i+3]
            cnt = 0
        if stocks[i] > stocks[i+1] > stocks[i+2] > stocks[i+3]:
            cnt += money // stocks[i+3]
            money %= stocks[i+3]
    return money + cnt * stocks[-1]


j = junhyeon(money, stocks)
s = sungmin(money, stocks)
if j > s:
    print("BNP")
elif j < s:
    print("TIMING")
else:
    print("SAMESAME")