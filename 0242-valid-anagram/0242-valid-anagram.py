class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        else:
            a="abcdefghijklmnopqrstuvwxyz"
            for i in a:
                if(s.count(i)!=t.count(i)):
                    return False
                    break
        return True
        