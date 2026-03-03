class Solution:
    def partitionString(self, s: str) -> int:
        visited=set()
        count=1
        for i in s:
            if i in visited:
                count+=1
                visited.clear()
            visited.add(i)
        return count    