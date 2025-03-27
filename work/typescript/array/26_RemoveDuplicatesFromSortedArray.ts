/*
 * @lc app=leetcode id=26 lang=typescript
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
function removeDuplicates(nums: number[]): number {
    let dump:number=0;
    let i:number=0;
    while(true){
        let j:number=i+1+dump;
        while(j<nums.length){
            if(nums[i]==nums[j]){
                j++;
            }
            else{
                [nums[i+1],nums[j]]=[nums[j],nums[i+1]];
                dump=j-i-1;
                break;
            };
        }
        if(j>=nums.length){
            return i+1;
        };
        i++;
    }
};
// @lc code=end

