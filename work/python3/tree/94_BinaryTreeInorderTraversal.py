#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def inorder(root: Optional[TreeNode], result: list[int]):
            if root:
                inorder(root.left,result)
                result.append(root.val)
                inorder(root.right,result)
            return result
        
        return inorder(root,result)
        
# @lc code=end

