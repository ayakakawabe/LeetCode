#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_node=ListNode()
        cur_node=result_node
        while list1 or list2:
            if not list1:
                cur_node.next=list2
                break
            elif not list2:
                cur_node.next=list1
                break
            else:
                if list1.val <= list2.val:
                    cur_node.next=ListNode(val=list1.val)
                    list1=list1.next
                else:
                    cur_node.next=ListNode(val=list2.val)
                    list2=list2.next
                cur_node=cur_node.next
        
        return result_node.next
        
# @lc code=end

