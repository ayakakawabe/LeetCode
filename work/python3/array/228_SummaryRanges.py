#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            consecutive_symbol="->"
            first_consecutive=None
            smallest_nums=[]
            for  i in range(0,len(nums)-1,1):
                if nums[i] + 1 == nums[i+1]:
                    if first_consecutive == None:
                        first_consecutive=nums[i]
                else:
                    if first_consecutive != None:
                        smallest_nums.append(str(first_consecutive)+consecutive_symbol+str(nums[i]))
                        first_consecutive=None
                    else:
                        smallest_nums.append(str(nums[i]))
            if first_consecutive == None:
                smallest_nums.append(str(nums[i+1]))
            else:
                smallest_nums.append(str(first_consecutive)+consecutive_symbol+str(nums[i+1]))
            return smallest_nums
# @lc code=end

