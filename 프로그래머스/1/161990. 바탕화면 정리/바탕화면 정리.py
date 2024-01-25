def solution(wallpaper):
    x_idx = []
    y_idx = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                x_idx.append(i)
                y_idx.append(wallpaper[i].find("#"))
                y_idx.append(wallpaper[i].rfind("#"))
    return [min(x_idx), min(y_idx), max(x_idx)+1, max(y_idx)+1]