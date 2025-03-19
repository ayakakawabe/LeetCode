#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber=0
        for i in range(0,len(columnTitle),1):
            columnNumber=columnNumber+26**((len(columnTitle)-1)-i)*(ord(columnTitle[i])-64)
        return columnNumber
# @lc code=end

