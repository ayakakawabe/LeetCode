#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        str_to_num_dict={
            "d":0,
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result=0
        index=0
        s_dummy=s+"d"
        while index<len(s):
            if str_to_num_dict[s_dummy[index]]>=str_to_num_dict[s_dummy[index+1]]:
                result=result+str_to_num_dict[s_dummy[index]]
                index=index+1
            else:
                result=result+(str_to_num_dict[s_dummy[index+1]]-str_to_num_dict[s_dummy[index]])
                index=index+2
        return result
# @lc code=end

