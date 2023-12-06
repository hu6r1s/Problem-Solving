x_li = []
y_li = []
for _ in range(3):
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)
for x in x_li:
    if x_li.count(x) == 1:
        res_x = x
for y in y_li:
    if y_li.count(y) == 1:
        res_y = y
print(res_x, res_y)