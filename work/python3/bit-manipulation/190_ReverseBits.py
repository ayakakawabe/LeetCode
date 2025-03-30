#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_b_n=""
        while n>1:
            reverse_b_n=reverse_b_n+str(n%2)
            n=int(n/2)
        reverse_b_n=reverse_b_n+str(n)
        reverse_b_n=reverse_b_n+"0"*(32-len(reverse_b_n))
        return int(reverse_b_n,2)
# @lc code=end

