#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target_node=head
        while target_node:
            target_val=target_node.val
            pre_node=target_node
            cur_node=target_node.next
            is_uniq=True
            while cur_node:
                if cur_node.val == target_val:
                    is_uniq=False
                    cur_node=cur_node.next
                else:
                    break
            
            if not is_uniq:
                pre_node.next=cur_node
            
            target_node=target_node.next


        return head


        
# @lc code=end

