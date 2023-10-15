############Problem: contains duplicate
#Approach 1: Brute Force
#since we are comparing nxn times therefore, Time complexity = O(n^2) and no extra memory so Space = O(1)

class Solution:
    def containsDuplicate(self, nums) -> bool:
        var = len(nums)
        for i in range(var):
            for j in range(var):
                if i!=j and nums[i] == nums[j]:
                    return True
        return False

S = Solution([1,2,1,3])
print(S)

#Approach 2: sorting
#since sorting takes time, Time complexity = O(nlogn) and space = O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        var = len(nums)
        nums.sort()
        for i in range(1,var):
            #for j in range(var):
            if nums[i-1] == nums[i]:
                return True
        return False

#Approach 3: Hash Map(array)
#As it checks each comparison operation is O(1), Therefore Time complexity = O(n), space = O(n) ? Because extra variables will take up to the size of the list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        var = []
        for i in nums:
            if i in var:
                return True
            var.append(i)
        return False
