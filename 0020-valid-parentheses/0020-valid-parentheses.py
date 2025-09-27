class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mappings={"]":"[",")":"(","}":"{"}
        stack=[]
        for i in s:
            if i in mappings:
                top_element=stack.pop() if stack else "#"
                if top_element!=mappings[i]:
                    return False
            else:
                stack.append(i)
        return len(stack)==0


        
        