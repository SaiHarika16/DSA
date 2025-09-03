class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]+nums[i+1]>nums[i+2] and nums[i+1]+nums[i+2]>nums[i] and nums[i+2]+nums[i]>nums[i+1]):
                if(nums[i]==nums[i+1]==nums[i+2]):
                    return "equilateral"
                elif(nums[i]<nums[i+1]<nums[i+2]):
                    return "scalene"
                elif(nums[i]==nums[i+1] or nums[i+1]==nums[i+2]):
                    return "isosceles"
            return "none"
        