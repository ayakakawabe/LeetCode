#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        sum_nums=[]
        while not n in sum_nums:
            if n == 1:
                return True
            sum_nums.append(n)
            NUM_FOR_CALC_DIGIT=10
            tmp_for_digit=n
            n=0
            while tmp_for_digit != 0:
                digit=tmp_for_digit%NUM_FOR_CALC_DIGIT
                tmp_for_digit=int(tmp_for_digit/NUM_FOR_CALC_DIGIT)
                n=n+digit**2
        return False
# @lc code=end

