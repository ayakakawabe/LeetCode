#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def calc_min_depth(root: Optional[TreeNode], min_depth: int, depth: int):
            if root:
                    depth=depth+1
                    if not root.left and not root.right:
                         if min_depth:
                            return min(min_depth,depth),depth
                         else:
                              return depth,depth
                    else:
                         min_depth,left_depth=calc_min_depth(root.left,min_depth,depth)
                         min_depth,right_depth=calc_min_depth(root.right,min_depth,depth)
                         return min_depth,max(left_depth,right_depth)
            return min_depth,depth
        
        if root:
            return calc_min_depth(root,None,0)[0]
        else:
            return 0
# @lc code=end

