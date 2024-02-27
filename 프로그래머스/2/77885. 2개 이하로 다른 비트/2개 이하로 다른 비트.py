def solution(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num+1)
        else:
            b = "0" + bin(num)[2:]
            b = b[:b.rindex("0")] + "10" + b[b.rindex("0")+2:]
            result.append(int(b, 2))
    return result