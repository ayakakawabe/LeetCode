#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count_depth_by_preorder(root: Optional[TreeNode], depth: int) -> int:
            if root:
                depth=depth+1
                left_depth=count_depth_by_preorder(root.left,depth)
                right_depth=count_depth_by_preorder(root.right,depth)
                return max(left_depth,right_depth)
            else:
                return depth
        
        return count_depth_by_preorder(root,0)
# @lc code=end

