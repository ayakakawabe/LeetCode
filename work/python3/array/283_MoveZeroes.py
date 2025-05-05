#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_sorted=-1
        index_unsorted=0
        while index_unsorted < len(nums):
            if nums[index_unsorted] != 0:
                index_sorted=index_sorted+1
                nums[index_sorted],nums[index_unsorted] = nums[index_unsorted],nums[index_sorted]
            index_unsorted=index_unsorted+1
                
# @lc code=end

