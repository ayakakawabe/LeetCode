#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1,1):
            for j in range(i+1,len(nums),1):
                two_sum=nums[i]+nums[j]
                if two_sum==target:
                    return [i,j]
        
# @lc code=end

