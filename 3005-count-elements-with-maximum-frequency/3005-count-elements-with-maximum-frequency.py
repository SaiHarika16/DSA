class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq=0
        res=0
        for i in nums:
            max_freq=max(nums.count(i),max_freq)
        for num in set(nums):
            if nums.count(num)==max_freq:
                res+=max_freq
        return res
        