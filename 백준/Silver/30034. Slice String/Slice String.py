N = int(input())
char_delimiters = set(input().split())
M = int(input())
num_delimiters = set(input().split())
K = int(input())
merge_chars = set(input().split())
S = int(input())
text = input()
delimiters = (char_delimiters | num_delimiters | {' '}) - merge_chars

tokens = []
current = ''

for ch in text:
    if ch in delimiters:
        if current:
            tokens.append(current)
            current = ''
    else:
        current += ch

if current:
    tokens.append(current)

for token in tokens:
    print(token)
