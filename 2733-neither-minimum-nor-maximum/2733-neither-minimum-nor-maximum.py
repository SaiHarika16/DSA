class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_nums=max(nums)
        min_nums=min(nums)
        for i in range(len(nums)):
            if nums[i]!=max_nums and nums[i]!=min_nums:
                return nums[i]
        return -1