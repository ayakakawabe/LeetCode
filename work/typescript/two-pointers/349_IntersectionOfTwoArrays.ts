/*
 * @lc app=leetcode id=349 lang=typescript
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
function intersection(nums1: number[], nums2: number[]): number[] {
    const result:Array<number>=[];
    for(let iNums1:number=0;iNums1<nums1.length;iNums1++){
        if(!result.includes(nums1[iNums1])){
            for(let iNums2:number=0;iNums2<nums2.length;iNums2++){
                if(nums1[iNums1]===nums2[iNums2]){
                    result.push(nums1[iNums1]);
                    break;
                };
            };
        };
    }
    return result;
};
// @lc code=end

