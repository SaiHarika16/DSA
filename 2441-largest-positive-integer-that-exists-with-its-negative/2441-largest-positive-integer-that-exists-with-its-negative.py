class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if not nums:
            return -1
        max_num=max(nums)
        if -1*max_num in nums:
            return max_num
        else:
            nums.remove(max_num)
            return self.findMaxK(nums)
        