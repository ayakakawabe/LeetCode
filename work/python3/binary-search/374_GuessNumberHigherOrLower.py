#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_num = 1
        max_num = n
        guess_num = int(n/2)

        def calc_guess_num(min_num,max_num):
            return min_num + int((max_num - min_num + 1) / 2)
        
        while True:
            guess_result = guess(guess_num)
            if guess_result == -1:
                # Guess a lower num.
                max_num = guess_num - 1
                guess_num = calc_guess_num(min_num,max_num)
            elif guess_result == 1:
                # Guess a higher num.
                min_num = guess_num + 1
                guess_num = calc_guess_num(min_num,max_num)
            else:
                return guess_num
# @lc code=end

