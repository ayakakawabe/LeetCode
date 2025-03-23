#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col_title=""
        while True:
            columnNumber=columnNumber-1
            col_title=chr(65+(columnNumber)%26)+col_title
            columnNumber=int((columnNumber)/26)
            if columnNumber == 0:
                break
        return col_title
# @lc code=end

