#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find median index
        if len(nums)%2 == 0:
            cur_check=len(nums)//2-1
        else:
            cur_check=len(nums)//2
        
        if nums[0] > target:
            return 0
        elif nums[len(nums)-1] < target:
            return len(nums)
        else:
            pre_check=-1
            while True:
                if nums[cur_check] < target:
                    cur_check=cur_check+1
                    if pre_check == cur_check:
                        return cur_check
                    pre_check=cur_check-1
                elif nums[cur_check] > target:
                    cur_check=cur_check-1
                    if pre_check == cur_check:
                        return cur_check+1
                    pre_check=cur_check+1
                else:
                    return cur_check
        
# @lc code=end

