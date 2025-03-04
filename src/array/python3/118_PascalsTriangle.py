#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas_tri=[[1]]
        for i_row in range(1,numRows,1):
            col=[]
            for i_col in range(0,i_row+1,1):
                if i_col == 0 or i_col == i_row:
                    col.append(1)
                else:
                    col.append(pas_tri[i_row-1][i_col-1]+pas_tri[i_row-1][i_col])
            pas_tri.append(col)
        
        return pas_tri
        
# @lc code=end

