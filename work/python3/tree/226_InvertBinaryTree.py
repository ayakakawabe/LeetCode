#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            invertRoot: Optional[TreeNode] = TreeNode()

            def invertNodeByPreoder(root: Optional[TreeNode],invertRoot: Optional[TreeNode]) -> Optional[TreeNode]:
                if root:
                    invertRoot.val=root.val
                    print(root.val)
                    if root.left:
                        invertRoot.right=TreeNode()
                        invertNodeByPreoder(root.left,invertRoot.right)
                    if root.right:
                        invertRoot.left=TreeNode()
                        invertNodeByPreoder(root.right,invertRoot.left)
                return root

            invertNodeByPreoder(root,invertRoot)
            return invertRoot
        else:
            return None

# @lc code=end

