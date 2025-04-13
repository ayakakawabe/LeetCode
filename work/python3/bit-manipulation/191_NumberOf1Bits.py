#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n=bin(n)
        count_one=0
        for i in range(2,len(bin_n),1):
            if bin_n[i]=="1":
                count_one=count_one+1
        return count_one
# @lc code=end

