class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums)==2:
            nums.sort(reverse=True)
            return nums
        for i in range(0,len(nums),2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums
        