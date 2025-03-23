#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        max=nums[length-1]
        for i in range(0,length,1):
            if nums[i] != max:
                for j in range(i+1,length,1):
                    if nums[i] < nums [j]:
                        nums[i+1],nums[j]=nums[j],nums[i+1]
                        break
            else:
                break
        return i+1
            
        
# @lc code=end

