class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=float("-inf")
        second=float("-inf")
        third=float("-inf")
        for i in set(nums):
            if i>first:
                third=second
                second=first
                first=i
            elif first>i>second:
                third=second
                second=i
            elif second>i>third:
                third=i
        if third!=float("-inf"):
            return third
        return first