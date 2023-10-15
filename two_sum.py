###########Problem: Two Sum
#Approach1: Brute Force
#time complexity = O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i,j]
        return []
    
#Approach2: Brute force
#time complexity = O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
    
#Approach3: HashMap
#tc = O(n), sc = O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dicts:
                return [i,dicts[comp]]
            dicts[nums[i]] = i
        return []
