#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            pass
        elif m == 0:
            nums1[0:n]=nums2[0:n]
        else:
            cur_num1=0
            cur_num2=0
            while cur_num2 < n:
                while True:
                    if nums1[cur_num1] < nums2[cur_num2]:
                        cur_num1=cur_num1+1
                    else:
                        nums1[cur_num1],nums1[cur_num1+1:m+cur_num2+1]=nums2[cur_num2],nums1[cur_num1:m+cur_num2]
                        cur_num1=cur_num1+1
                        break
                    if cur_num1 >= m+cur_num2:
                        nums1[cur_num1:]=nums2[cur_num2:]
                        cur_num2=n
                        break
                cur_num2=cur_num2+1
# @lc code=end

