#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        square = int(num/2)
        product = square * square
        while product > num:
            square = int(square/2)
            product = square * square
       
        pre_square = square * 2
        while square < pre_square:
            if square * square == num:
                return True
            else:
                square += 1
        
        return False
# @lc code=end

