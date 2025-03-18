#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2 == 0:
            for i in range(0,int(len(nums)/2),1):
                if nums[i] == nums[i+int(len(nums)/2)]:
                    return nums[i]
        else:
            for i in range(0,int(len(nums)/2)+1,1):
                if nums[i] == nums[i+int(len(nums)/2)]:
                    return nums[i]

# @lc code=end

