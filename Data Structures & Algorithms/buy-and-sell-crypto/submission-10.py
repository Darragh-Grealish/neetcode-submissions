class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(0, len(prices)):
            for j in range(i, len(prices)-1):
                cal = prices[j+1] - prices[i]
                if cal > answer:
                    answer = cal
        return answer
