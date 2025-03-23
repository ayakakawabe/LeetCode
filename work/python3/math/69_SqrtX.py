#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        else:
            pre=0
            cur=1
            while True:
                if cur*cur < x:
                    pre=cur
                    cur=cur+1
                elif cur*cur > x:
                    return pre
                else:
                    return cur
        
# @lc code=end

