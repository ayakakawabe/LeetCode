/*
 * @lc app=leetcode id=21 lang=typescript
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const result:ListNode = new ListNode();
    let resultTmp:ListNode = result;
    while(list1 && list2){
        if(list1.val < list2.val){
            resultTmp.next = new ListNode(list1.val);
            list1=list1.next;
        }
        else{
            resultTmp.next = new ListNode(list2.val);
            list2=list2.next;
        };
        resultTmp=resultTmp.next;
    };
    if(list1){
        resultTmp.next=list1;
    };
    if(list2){
        resultTmp.next=list2;
    };
    return result.next;
}
// @lc code=end

