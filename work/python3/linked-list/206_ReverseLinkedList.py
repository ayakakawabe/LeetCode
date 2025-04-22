#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseHead=ListNode()
        def reverse(head,reverseHead):
            if head:
                reverseHead=reverse(head.next,reverseHead)
                reverseHead.next=ListNode(val=head.val)
                reverseHead=reverseHead.next
            return reverseHead

        reverse(head,reverseHead)
        return reverseHead.next
# @lc code=end

