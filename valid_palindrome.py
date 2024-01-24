#################valid palindrome
# Approach 1: Brute
# TC= O(n), SC = O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        var1 = ""
        for i in s.lower():
            if i.isalnum():
                var1 += i

        return var1 == var1[::-1]
