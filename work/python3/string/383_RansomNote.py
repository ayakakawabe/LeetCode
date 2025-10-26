#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter in magazine:
                for i in range(0, len(magazine), 1):
                    if letter == magazine[i]:
                        magazine = magazine[0:i]+magazine[i+1:]
                        break
            else:
                return False
        return True
# @lc code=end

