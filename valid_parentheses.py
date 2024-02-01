#Example for difference between and &
#a = 14
#b = 4
# 
#print(b and a)  # outputs 14: compiler checks b is 4 which is true then checks a is 14 which is also true. Instead of True, it'll return last checked variable value
#print(b & a)  # output 4: returns bitwise calculated result
#####################################################################################################################################################################
###Valid parentheses##
# TC = O(n) : Valid for sequecne/string like "()" or "()[]{}"
class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(0,len(s)-1):
            if (s[i] == "(") & (s[i+1] != ")"):
                return False
            elif (s[i] == "[") & (s[i+1] != "]"):
                return False
            elif (s[i] == "{") & (s[i+1] != "}"):
                return False
        return True if ("(" or "{" or "[") in s else False

#Approach: stack
#TC = O(n) : Return True if parantheses in correct order
class Solution:
    def isValid(self, s: str) -> bool:
        lt=[]
        dicts = {")":"(", "}":"{","]":"["}
        for i in s:
            if (i in dicts):
                if lt and (lt[-1] == dicts[i]):
                    lt.pop()
                else:
                    return False
            else:
                lt.append(i)
        return True if not lt else False
