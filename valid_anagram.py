#############Problem: Valid Anagram
#Approach1: sorting
#complexity in time = O(nlogn), space = O(1) -> depends
class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        return sorted(s) == sorted(t)

#Approach2: Hashmap table(dictionary)
# Time complexity = O(n); space = O(n)
class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        ctrs = {}
        if len(s) != len(t):
            return False
        for i in s:#counting frequency
            ctrs[i] = 1 + ctrs.get(i,0)#if key, value not there in hash then it'll give default value as 0
        for j in t:
            ctrs[j] = 1 + ctrs.get(j,0)
        for k in ctrs.values():
            if k%2 != 0:
                return False
        return True

#Approach3: array
# Time complexity = O(n); space = O(n)
class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        ctrs = [0]*26 #index positions for 26 alphabets
        for i in s:
            ctrs[i] += 1
        for j in t:
            ctrs[j] -= 1
        for i in ctrs.values():
            if i != 0:
                return False
        return True

#Approach4: Counter method (to count frequency)(it's a dict subclass)
#complexity in time = O(n), space = O(1)
class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        return Counter(s) == Counter(t)
