class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            lsum=sum(nums[:i])
            rsum=sum(nums[i+1:])
            if lsum==rsum:
                return i
        return -1