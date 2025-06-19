class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count=Counter(nums)
        return [item[0] for item in count.most_common(k)]
            