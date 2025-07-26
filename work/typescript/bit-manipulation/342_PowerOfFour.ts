/*
 * @lc app=leetcode id=342 lang=typescript
 *
 * [342] Power of Four
 */

// @lc code=start
function isPowerOfFour(n: number): boolean {
    if(n<=0){
        return false
    }else if(n==1){
        return true
    }else{
        while(n%4==0){
            n=Number(n/4)
        }
        if(n==1){
            return true
        }else{
            return false
        }
    }

};
// @lc code=end

