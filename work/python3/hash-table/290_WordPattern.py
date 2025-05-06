#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        maps={}
        s_list=s.split()
        if len(s_list) != len(pattern):
            return False
        for i in range(0,len(s_list),1):
            if pattern[i] not in maps.keys() and s_list[i] not in maps.values():
                maps[pattern[i]] = s_list[i]
            elif pattern[i] in maps.keys():
                if maps[pattern[i]] != s_list[i]:
                    return False
            else:
                return False
        return True
# @lc code=end

