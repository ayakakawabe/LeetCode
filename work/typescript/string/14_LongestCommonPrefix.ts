/*
 * @lc app=leetcode id=14 lang=typescript
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
function longestCommonPrefix(strs: string[]): string {
    strs.sort((a:string,b:string) => a.length-b.length);
    if(strs[0].length != 0){
        for(let lengthPrefix:number=strs[0].length;lengthPrefix>0;lengthPrefix--){
            const prefix:string=strs[0].slice(0,lengthPrefix);
            const expPrefix:RegExp=new RegExp('^'+prefix+'.*$');
            let hasPrefix:boolean=true;
            for(let iStrs:number=1;iStrs<strs.length;iStrs++){
                if(!expPrefix.test(strs[iStrs])){
                    hasPrefix=false;
                    break;
                }
            }
            if(hasPrefix){
                return prefix;
            }
        }
    }
    return "";
};
// @lc code=end

