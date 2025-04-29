#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp_num=0
            digits_rest=num
            while digits_rest != 0:
                tmp_num=tmp_num+digits_rest%10
                digits_rest=int(digits_rest/10)
            num=tmp_num
        return num
# @lc code=end

