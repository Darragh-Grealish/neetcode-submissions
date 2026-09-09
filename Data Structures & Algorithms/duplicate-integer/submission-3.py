class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = []
        for i in range(0, len(nums)):
            if nums[i] in a:
                return True
            else:
                a.append(nums[i])
        return False