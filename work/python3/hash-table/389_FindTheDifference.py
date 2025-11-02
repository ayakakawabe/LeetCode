#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if len(s) == 0:
                return letter
            i = s.find(letter)
            if i == -1:
                return letter
            else:
                s = s[:i] + s[i+1:]
# @lc code=end

