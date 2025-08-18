class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            res^=num
        return res
        