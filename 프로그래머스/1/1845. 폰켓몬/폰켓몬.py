def solution(nums):
    select = len(set(nums))
    if len(nums) // 2 <= select:
        return len(nums) // 2
    else:
        return select