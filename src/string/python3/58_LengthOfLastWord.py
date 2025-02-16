#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                if i != 0:
                    for j in range(i-1,-2,-1):
                        if j >=0:
                            if s[j] == " ":
                                return i-j
                        else:
                            return i+1
                else:
                    return 1
        
# @lc code=end

