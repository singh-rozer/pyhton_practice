# Approach 1: Brute
# TC= O(n^2), SC = O(1)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        counter = 1
        for i in nums:
            check = i+1
            for j in range(0,len(nums)):
                print("check = ",check)
                if check in nums:
                    counter += 1
                    check += 1
                else:
                    print("break : check = ",check,"counter = ",counter)
                    if counter > longest:
                        longest = counter
                    counter = 1
                    break
        return longest
