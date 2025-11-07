class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash={}
        for i in range(len(nums)):
            nums_hash[nums[i]]=i
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in nums_hash and i!=nums_hash[comp]:
                return i,nums_hash[comp] 
