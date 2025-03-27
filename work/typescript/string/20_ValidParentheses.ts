/*
 * @lc app=leetcode id=20 lang=typescript
 *
 * [20] Valid Parentheses
 */

// @lc code=start
function isValid(s: string): boolean {
    function pairOpenParenthes(closeParenthes: string): string{
        if(closeParenthes==")"){
            return "(";
        }
        else if(closeParenthes=="]"){
            return "[";
        }
        else{
            return "{";
        }
    };

    const stack:Array<string>=[];

    for(let i_s:number=0;i_s<s.length;i_s++){
        if(s[i_s]=="(" || s[i_s]=="[" || s[i_s]=="{"){
            stack.push(s[i_s]);
        }
        else{
            if(stack.length!=0 && pairOpenParenthes(s[i_s])==stack[stack.length-1]){
                stack.pop();
            }
            else{
                return false;
            }
        }
    }
    if(stack.length==0){
        return true;
    }
    else{
        return false;
    }
};
// @lc code=end

