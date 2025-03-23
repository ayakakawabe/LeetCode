#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # def quick_sort(array: List[int]) -> List[int]:
        #     if len(array) <= 1:
        #         return array
        #     piv=array.pop(0)
        #     left=[]
        #     right=[]
        #     for i in range(0,len(array),1):
        #         if array[i] <= piv:
        #             left.append(array[i])
        #         else:
        #             right.append(array[i])
        #     left=quick_sort(left)
        #     right=quick_sort(right)
        #     return left+[piv]+right
        
        # nums=quick_sort(nums)
        nums.sort()
        return nums[int(len(nums)/2)]
# @lc code=end

