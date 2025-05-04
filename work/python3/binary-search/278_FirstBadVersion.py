#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def nextCheckVersion(min,max) -> int:
            num_range=max-min+1
            if num_range%2 == 0:
                return min+int(num_range/2)-1
            else:
                return min+int(num_range/2)
        
        min_bad_version=1
        max_bad_version=n
        cur_check_version=nextCheckVersion(min_bad_version,max_bad_version)
        while min_bad_version != max_bad_version:
            if isBadVersion(cur_check_version):
                max_bad_version=cur_check_version
                cur_check_version=nextCheckVersion(min_bad_version,max_bad_version)
                
            else:
                min_bad_version=cur_check_version+1
                cur_check_version=nextCheckVersion(min_bad_version,max_bad_version)
                
        return min_bad_version                    
# @lc code=end

