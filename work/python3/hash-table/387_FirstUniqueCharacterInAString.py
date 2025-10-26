#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        notUniqChar = "-"
        for i in range(0, len(s), 1):
            if s[i] == notUniqChar:
                continue
            elif i == len(s)-1 or s[i] not in s[i+1:]:
                return i
            else:
                s = s.replace(s[i],notUniqChar)
        return -1  
# @lc code=end

