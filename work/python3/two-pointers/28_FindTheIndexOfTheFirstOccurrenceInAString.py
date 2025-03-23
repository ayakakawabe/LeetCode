#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result=-1
        if len(haystack) >= len(needle):
            for i in range(0,len(haystack)-len(needle)+1,1):
                if haystack[i] == needle[0]:
                    needle_index=1
                    while needle_index < len(needle):
                        if haystack[i+needle_index] == needle[needle_index]:
                            needle_index=needle_index+1
                        else:
                            break
                    if needle_index == len(needle):
                        result=i
                        break
                        
        return result
        
# @lc code=end

