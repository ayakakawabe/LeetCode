#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def getIntersection(shorterArray,longerArray):
            resultArray=[]
            for i in range(0,len(shorterArray),1):
                for j in range(0,len(longerArray),1):
                    if longerArray[j] != -1 and shorterArray[i] == longerArray[j]:
                        resultArray.append(shorterArray[i])
                        longerArray[j]=-1
                        break
            return resultArray
        
        if len(nums1) <= len(nums2):
            return getIntersection(nums1,nums2)
        else:
            return getIntersection(nums2,nums1)
# @lc code=end

