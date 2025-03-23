#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Calculate combination.
        def cmb(n: int, r: int) -> int:
            top=1
            for i in range(n,n-r,-1):
                top=top*i
            bottom=1
            for j in range(r,0,-1):
                bottom=bottom*j
            return int(top/bottom)

        if n <= 3:
            return n
        else:
            if n%2 == 0:
                num_ways=2 # it's included two ways (when you only use 1 step, and only use 2 steps). 
                num_only_two_steps=int(n/2) # When you only use 2 steps, a number that you climb until you reach the top.
                for k in range(1,num_only_two_steps,1):
                    num_ways=num_ways+cmb(n-k,k)
            else:
                num_ways=1 # it's included one way (when you only use 1 step).
                num_most_two_steps=int(n/2) # When you use 2 steps as well as possible, a number that you climb by two steps until you reach the top.
                for k in range(1,num_most_two_steps+1,1):
                    num_ways=num_ways+cmb(n-k,k)
        
            return num_ways

        
# @lc code=end

