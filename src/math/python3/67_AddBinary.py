#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Complement "0"
        if len(a) < len(b):
            a="0"*(len(b)-len(a))+a
        elif len(a) > len(b):
            b="0"*(len(a)-len(b))+b
        
        ans=""
        i=len(a)-1
        carry=0
        while True:
            one_digit_sum=int(a[i])+int(b[i])+carry
            if one_digit_sum > 1:
                ans=str(one_digit_sum-2)+ans
                carry=1
            else:
                ans=str(one_digit_sum)+ans
                carry=0
            i=i-1
            if i < 0:
                if carry == 0:
                    return ans
                else:
                    return str(carry)+ans
        
# @lc code=end

