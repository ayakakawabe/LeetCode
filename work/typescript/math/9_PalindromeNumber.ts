/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    if(x==0){
        return true
    }
    else if(x<0){
        return false
    }
    else{
        let tmp_x:number=x
        let reverse_x:number=0
        while(tmp_x!=0){
            reverse_x=tmp_x%10+reverse_x*10
            tmp_x=Math.floor(tmp_x/10)
        }
        return x==reverse_x
    }
};
// @lc code=end

