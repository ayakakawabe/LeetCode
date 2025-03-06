#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.append("dummy")
        while nums[1] != "dummy":
            j=1
            while True:
                if nums[j] == "dummy":
                    return nums[0]
                elif nums[0] == nums[j]:
                    nums.pop(0)
                    nums.pop(j-1)
                    break
                else:
                    j=j+1
        return nums[0]
# @lc code=end

