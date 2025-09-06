class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count=0
        count=0
        for i in nums:
            if i==1:
                curr_count+=1
            else:
                count=max(count,curr_count)
                curr_count=0
        count=max(count,curr_count)
        return count

        