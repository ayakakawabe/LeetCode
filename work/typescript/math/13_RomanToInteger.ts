/*
 * @lc app=leetcode id=13 lang=typescript
 *
 * [13] Roman to Integer
 */

// @lc code=start
function romanToInt(s: string): number {
    const symbols: {[key: string]: number} = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    let result:number = 0
    while(s.length > 1){
        if(symbols[s[0]] < symbols[s[1]]){
            result+=symbols[s[1]]-symbols[s[0]]
            s=s.slice(2)
        }
        else{
            result+=symbols[s[0]]
            s=s.slice(1)
        }
    }
    if(s.length == 1){
        result+=symbols[s[0]]
    }
    return result
};
// @lc code=end

