/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
    for( let i: number = 0; i < nums.length-1; i++){
        for(let j :number = i+1; j < nums.length; j++){
            if(nums[i]+nums[j] == target){
                return [i,j]
            }
        }
    }
};
// @lc code=end

