#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(root_left: Optional[TreeNode],root_right :Optional[TreeNode],is_continue : bool) -> bool:
            if is_continue:
                if root_left and root_right:
                    if root_left.val != root_right.val:
                        return False
                    else:
                        is_continue=is_mirror(root_left.left,root_right.right,is_continue)
                        is_continue=is_mirror(root_left.right,root_right.left,is_continue)
                elif not root_left and not root_right:
                    pass
                else:
                    return False
            return is_continue
        
        return is_mirror(root.left,root.right,True)
# @lc code=end

