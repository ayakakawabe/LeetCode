/*
 * @lc app=leetcode id=35 lang=typescript
 *
 * [35] Search Insert Position
 */

// @lc code=start
function searchInsert(nums: number[], target: number): number {
    let isPreLow:boolean|undefined;
    let i:number=Math.floor(nums.length/2);
    while(0<=i && i<nums.length){
        if(nums[i]<target){
            if(isPreLow==false){
                return i+1;
            }
            else{
                isPreLow=true;
                i++;
            };
        }
        else if(target<nums[i]){
            if(isPreLow===true){
                return i;
            }
            else{
                isPreLow=false;
                i--;
            };
        }
        else{
            return i;
        }
    };
    if(i==-1){
        return 0;
    }
    else{
        return i;
    }
};
// @lc code=end

