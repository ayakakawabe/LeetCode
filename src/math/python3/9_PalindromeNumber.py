#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x>0:
            divisor=x
            dividend=10
            num_array=[]
            while divisor>=1:
                remainder=divisor%dividend
                num_array.append(remainder)
                divisor=int(divisor/dividend)
            
            if num_array[0]==0:
                return False
            else:
                backward=0
                for i in range(0,len(num_array),1):
                    if i==len(num_array)-1:
                        backward=backward+num_array[0]
                    else:
                        backward=backward+dividend**(len(num_array)-1-i)*num_array[i]
                
                if backward==x:
                    return True
                else:
                    return False
        else:
            return True
                    
        
# @lc code=end

