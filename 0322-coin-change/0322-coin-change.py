from collections import deque

class Solution:
    """
    1. 가장 큰 수부터 차례대로 빼면서 확인 - 틀린 풀이
    가장 큰 수부터 차례대로 빼면 안되는 경우가 있음
    coins = [186,419,83,408], amount = 6249
    이건 419부터 안될때까지 빼는 방식으로 되지 않음, 즉 최적의 금액을 찾아야 함.
    그리디 같은 문제일 듯

    """
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        result = 0
        for coin in coins:
            while amount >= coin:
                amount -= coin
                result += 1
        
        if amount:
            return -1
        return result
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        def bfs():
            queue = deque([(0, 0)])
            visited = set()
            while queue:
                cnt, total = queue.popleft()
                if amount == total:
                    return cnt
                if total in visited:
                    continue
                visited.add(total)

                for coin in coins:
                    if coin + total <= amount:
                        queue.append((cnt + 1, total + coin))
            return -1
        
        return bfs()