#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def comparePreAdresses(head: Optional[ListNode]) -> bool:
            pre_adresses=[]
            while head:
                if id(head) in pre_adresses:
                    return True
                else:
                    pre_adresses.append(id(head))
                    head=head.next
            return False
        
        def compareSlowAndFastPointer(head: Optional[ListNode]) -> bool:
            if head:
                slow_head=head
                fast_head=head.next
                while slow_head and fast_head:
                    if id(slow_head) == id(fast_head):
                        return True
                    elif fast_head.next:
                        slow_head=slow_head.next
                        fast_head=fast_head.next.next
                    else:
                        break
            return False
            
        return compareSlowAndFastPointer(head)
# @lc code=end

