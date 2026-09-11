class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort(reverse=True)
            print(stones[0])
            print(stones[1])
            if stones[0] == stones[1]:
                stones.remove(stones[1])
                stones.remove(stones[0])
            else:
                if stones[0] > stones[1]:
                    stones[0] = stones[0] - stones[1]
                    stones.remove(stones[1])
                else:
                    stones[1] = stones[1] - stones[0]
                    stones.remove(stones[0])
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
