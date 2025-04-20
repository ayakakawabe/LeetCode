#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap=dict()
        for i in range(0,len(s),1):
            if (s[i] not in charMap.keys()) and (t[i] not in charMap.values()):
                charMap[s[i]]=t[i]
            else:
                if (s[i] in charMap.keys()) and (charMap[s[i]] == t[i]):
                    pass
                else:
                    return False
        return True
    # @lc code=end

