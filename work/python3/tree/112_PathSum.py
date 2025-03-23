#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def compare_sum_nodes(root: Optional[TreeNode], sum_nodes: int, is_same: bool) -> tuple[int,bool]:
            if root:
                if is_same:
                    return sum_nodes,is_same
                else:
                    sum_nodes=sum_nodes+root.val
                    if sum_nodes == targetSum and not root.left and not root.right:
                        return sum_nodes,True
                    else:
                        if not root.left and not root.right:
                            return sum_nodes-root.val,is_same
                        is_same=compare_sum_nodes(root.left,sum_nodes,is_same)[1]
                        if is_same:
                            return sum_nodes,is_same
                        is_same=compare_sum_nodes(root.right,sum_nodes,is_same)[1]
            return sum_nodes,is_same
        
        return compare_sum_nodes(root,0,False)[1]
# @lc code=end

