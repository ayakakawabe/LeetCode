#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def tree_height(root : Optional[TreeNode],height: int,is_balanced: bool):
            if root:
                left_height,is_balanced=tree_height(root.left,height+1,is_balanced)
                right_height,is_balanced=tree_height(root.right,height+1,is_balanced)
                if is_balanced:
                    return max(left_height,right_height),abs(left_height-right_height) <= 1
            return height,is_balanced
        
        return tree_height(root,0,True)[1]
        # @lc code=end

