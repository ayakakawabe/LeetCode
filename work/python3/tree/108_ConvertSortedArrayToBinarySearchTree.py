#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        node=TreeNode()
        
        def append_node(nums: list[int], root: Optional[TreeNode]) -> Optional[TreeNode]:
            if len(nums) != 0:
                append_nums_index=int(len(nums)/2)
                root=TreeNode(nums[append_nums_index])
                if 0 < append_nums_index:
                    root.left=append_node(nums[0:append_nums_index],root.left)
                if append_nums_index < len(nums)-1:
                    root.right=append_node(nums[append_nums_index+1:],root.right)
            return root
        
        return append_node(nums,node)
# @lc code=end

