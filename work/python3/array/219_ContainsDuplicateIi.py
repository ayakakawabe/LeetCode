#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)<=1 or k==0:
            return False
        else:
            if k<len(nums):
                for i in range(0,len(nums)-1,1):
                    for j in range(i+1,min(i+k+1,len(nums)),1):
                        if(nums[i]==nums[j]):
                            return True
            else:
                for i in range(0,len(nums)-1,1):
                    for j in range(i+1,len(nums),1):
                        if(nums[i]==nums[j]):
                            return True
            return False
# @lc code=end

