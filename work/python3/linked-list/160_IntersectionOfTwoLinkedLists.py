#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA_adresses=[]
        while headA:
            headA_adresses.append(id(headA))
            headA=headA.next
        
        while headB:
            if id(headB) in headA_adresses:
                return headB
            else:
                headB=headB.next
        return None
        
# @lc code=end

