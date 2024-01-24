###############Problem: two sum, in which input array is sorted and index should start with 1 instead of 0
# Approach 1: two pointer
#one pointer starts from leftmost and another from rightmost.
#depends on sum the pointer will move
#TC = O(n), SC = O(n)
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while i<j:
            sumt = numbers[i]+numbers[j]
            if sumt == target:
                return i+1,j+1
            if sumt > target:
                j=j-1
                print("chek1")
            else:
                i=i+1
                print("check2")
        return
