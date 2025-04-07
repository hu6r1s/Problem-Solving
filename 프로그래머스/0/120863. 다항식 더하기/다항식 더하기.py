def solution(polynomial):
    x, y = 0, 0
    polynomial = polynomial.split(" + ")
    for poly in polynomial:
        if 'x' in poly:
            x += 1 if poly == "x" else int(poly[:-1])
        else:
            y += int(poly)
    
    if not x:
        return str(y)
    elif not y:
        return f"{x}x" if x != 1 else "x"
    else:
        return f"{x}x + {y}" if x != 1 else f"x + {y}"