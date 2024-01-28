#Approach 1:
#TC = O(n) SC = O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt=[]
        res = 0
        for i in s:
            if i not in lt:
                lt.append(i)
            else:
                res = max(res, len(lt)) #before starting new substring set calculating the length
                lt = []
                lt.append(i)
        return res
