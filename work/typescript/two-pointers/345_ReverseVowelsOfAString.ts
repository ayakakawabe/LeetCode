/*
 * @lc app=leetcode id=345 lang=typescript
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start
function reverseVowels(s: string): string {
    const vowels:Array<string>=["a","i","u","e","o","A","I","U","E","O"];
    let headResult:string="";
    let tailResult:string="";
    let indexFromHead:number=0;
    let indexFromTail:number=s.length-1;
    while(indexFromHead<=indexFromTail){
        if(vowels.includes(s[indexFromHead])){
            while(indexFromHead<=indexFromTail){
                if(indexFromHead===indexFromTail){
                    headResult+=s[indexFromHead];
                    indexFromTail--;
                    break;
                }else if(vowels.includes(s[indexFromTail])){
                    headResult+=s[indexFromTail];
                    tailResult=s[indexFromHead]+tailResult;
                    indexFromTail--;
                    break;
                }else{
                    tailResult=s[indexFromTail]+tailResult;
                    indexFromTail--;
                };
            };
        }else{
            headResult+=s[indexFromHead];
        };
        indexFromHead++;
    };
    return headResult+tailResult;
};
// @lc code=end

