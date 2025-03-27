/*
 * @lc app=leetcode id=26 lang=typescript
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
function removeDuplicates(nums: number[]): number {
    if(nums.length==1){
        return 1;
    }
    else{
        let i:number=1;
        let numDoubtUniq:number=nums[0];
        while(i<nums.length){
            if(numDoubtUniq==nums[i]){
                nums.splice(i,1);
            }
            else{
                numDoubtUniq=nums[i];
                i++;
            };
        };
        return nums.length;
    };
};
// @lc code=end

