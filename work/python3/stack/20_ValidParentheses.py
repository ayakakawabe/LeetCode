#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        def convertBracketsToLetters(brackets:str)->str:
            if brackets=="(":
                return "open1"
            elif brackets==")":
                return "close1"
            elif brackets=="{":
                return "open2"
            elif brackets=="}":
                return "close2"
            elif brackets=="[":
                return "open3"
            elif brackets=="]":
                return "close3"
        
        brackets_pares={
            "open1":"close1",
            "open2":"close2",
            "open3":"close3"
        }

        stack_list=[]
        for i in range(0,len(s),1):
            if convertBracketsToLetters(s[i]) in brackets_pares.keys():
                stack_list.append(convertBracketsToLetters(s[i]))
            else:
                if len(stack_list)==0:
                    return False
                elif brackets_pares[stack_list[len(stack_list)-1]]==convertBracketsToLetters(s[i]):
                    stack_list.pop(len(stack_list)-1)
                else:
                    return False
        if len(stack_list)==0:
            return True
        else:
            return False
    
                
        
# @lc code=end

