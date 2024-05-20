#Approach 1: Brute
#TC = O(nlogn)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1+nums2
        num3 = sorted(num3)
        l = len(num3)
        median = l//2
        if l%2 != 0:
            print(num3)
            return num3[median]
        else:
            print(num3)
            return (num3[median-1]+num3[median])/2.0
