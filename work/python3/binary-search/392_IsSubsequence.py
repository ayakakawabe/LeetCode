#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        for letter in s:
            if len(t) == 0:
                return False
            i_t = t.find(letter)
            if i_t == -1:
                return False
            else:
                t = t[i_t+1:]
        return True
# @lc code=end

