#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder_compare(root1,root2,is_same):
            if is_same:
                if root1 and root2:
                    if root1.val != root2.val:
                        is_same=False
                    else:
                        is_same=preorder_compare(root1.left,root2.left,is_same)
                        is_same=preorder_compare(root1.right,root2.right,is_same)
                elif not root1 and not root2:
                    pass
                else:
                    is_same=False
            return is_same
            
        return preorder_compare(p,q,True)

# @lc code=end

