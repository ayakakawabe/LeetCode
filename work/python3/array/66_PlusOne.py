#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+1 != 10:
                digits[i]=digits[i]+1
                return digits
            else:
                digits[i]=0
                if i == 0:
                    return [1]+digits
        
# @lc code=end

