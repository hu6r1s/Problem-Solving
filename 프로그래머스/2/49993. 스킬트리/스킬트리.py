def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        skill_q = list(skill)
        for tree in skill_tree:
            if tree in skill_q:
                if tree != skill_q.pop(0):
                    break
        else:
            cnt += 1
    return cnt