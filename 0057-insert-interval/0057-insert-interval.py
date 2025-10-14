class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        output = [intervals[0]]
        for x, y in intervals[1:]:
            if output[-1][1] >= x:
                output[-1][1] = max(y, output[-1][1])
            else:
                output.append([x, y])
        return output