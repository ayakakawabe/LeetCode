#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_uncheck=len(nums)-1
        current_check=0
        k=0
        while current_check <= last_uncheck:
            if nums[current_check] == val:
                nums[current_check],nums[last_uncheck]=nums[last_uncheck],nums[current_check]
                last_uncheck=last_uncheck-1
            else:
                k=k+1
                current_check=current_check+1
        
        return k

        
# @lc code=end

