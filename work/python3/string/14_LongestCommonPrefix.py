#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Search shortest length in input.
        shortest_len=200
        for i in range(0,len(strs),1):
            if len(strs[i])<shortest_len:
                shortest_len=len(strs[i])

        # Search common prefix
        result=""
        for j in range(0,shortest_len,1):
            compare_letter=strs[0][j]
            is_match=True
            for k in range(1,len(strs),1):
                if strs[k][j]!=compare_letter:
                    is_match=False
                    break

            if is_match:
                result=result+compare_letter
            else:
                break
        
        return result

        
# @lc code=end

