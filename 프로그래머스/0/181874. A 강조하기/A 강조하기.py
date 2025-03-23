def solution(myString):
    myString = myString.replace('a', 'A')
    return "".join([string.lower() if string != 'A' else string for string in myString ])