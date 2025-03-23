#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert str "s" to lowercase and num.
        alphanum_list=re.findall("[a-zA-Z0-9]+",s)
        lowercase_num_s=""
        for i in range(0,len(alphanum_list),1):
            lowercase_num_s=lowercase_num_s+str.lower(alphanum_list[i])
        
        # Check if it's a palindrome.
        len_s=len(lowercase_num_s)
        if len_s <= 1:
            return True
        else:
            for j in range(0,int(len_s/2),1):
                if lowercase_num_s[j] != lowercase_num_s[len_s-1-j]:
                    return False
            return True
# @lc code=end

