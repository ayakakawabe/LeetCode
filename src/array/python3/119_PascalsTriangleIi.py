#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            pre_row=[1,1]
            for i_row in range(2,rowIndex+1,1):
                cur_row=[]
                for i_col in range(0,i_row+1,1):
                    if i_col == 0 or i_col == i_row:
                        cur_row.append(1)
                    else:
                        cur_row.append(pre_row[i_col-1]+pre_row[i_col])
                if i_row != rowIndex:
                    pre_row=cur_row
            return cur_row
# @lc code=end

