#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead= ListNode()
        curHead=newHead
        while head:
            if head.val != val:
                curHead.next=ListNode(head.val)
                curHead=curHead.next
            head=head.next
        return newHead.next
# @lc code=end

