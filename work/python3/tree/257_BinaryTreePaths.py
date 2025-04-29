#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths=[]
        def preorder(root: Optional[TreeNode] ,path: str) -> str:
            if root:
                if not root.left and not root.right:
                    paths.append(path+str(root.val))
                else:
                    path=path+str(root.val)+"->"
                    preorder(root.left,path)
                    preorder(root.right,path)
        preorder(root,"")
        return paths
# @lc code=end

