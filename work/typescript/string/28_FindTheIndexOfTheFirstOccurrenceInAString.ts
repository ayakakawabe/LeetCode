/*
 * @lc app=leetcode id=28 lang=typescript
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
function strStr(haystack: string, needle: string): number {
    const len_needle:number=needle.length
    let i:number=0;
    while(i <= haystack.length-len_needle){
        if(haystack.slice(i,i+len_needle)==needle){
            return i;
        }
        else{
            i++;
        };
    };
    return -1;
};
// @lc code=end

