class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        curr_s=""
        for i in words:
            curr_s+=i
            if curr_s==s:
                return True
        return False
        