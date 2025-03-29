/*
 * @lc app=leetcode id=27 lang=typescript
 *
 * [27] Remove Element
 */

// @lc code=start
function removeElement(nums: number[], val: number): number {
    let k:number=nums.length-1;
    let i:number=0;
    while(i<=k){
        if(nums[i]==val){
            [nums[i],nums[k]]=[nums[k],nums[i]];
            k--;
        }
        else{
            i++
        };
    };
    return k+1;
};
// @lc code=end

