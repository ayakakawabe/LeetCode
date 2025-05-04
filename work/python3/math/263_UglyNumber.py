#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n in [1,2,3,5]:
            return True
        else:
            import math
            n=abs(n)
            for i in range(2,int(math.sqrt(n))+1):
                while n%i == 0:
                    if i > 5:
                        return False
                    n=int(n/i)
            if n > 5:
                return False
            else:
                return True
# @lc code=end

