def solution(nums):
    count = set(nums)
    if len(nums) // 2 > len(count):
        return len(count)
    else:
        return len(nums) // 2