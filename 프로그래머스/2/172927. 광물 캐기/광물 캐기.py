def solution(picks, minerals):
    result = 0
    diamond, iron, stone = picks
    diamond_re = {"diamond": 1, "iron": 1, "stone": 1}
    iron_re = {"diamond": 5, "iron": 1, "stone": 1}
    stone_re = {"diamond": 25, "iron": 5, "stone": 1}
    
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]
    minerals.sort(reverse=True, key=lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")))

    for mineral in minerals:
        if diamond > 0:
            for i in mineral:
                result += diamond_re[i]
            diamond -= 1
        elif iron > 0:
            for i in mineral:
                result += iron_re[i]
            iron -= 1
        elif stone > 0:
            for i in mineral:
                result += stone_re[i]
            stone -= 1
    return result