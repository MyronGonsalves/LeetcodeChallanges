# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

 

# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:

# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 231 - 1
# 1 <= pick <= n
# Accepted 523K Submissions 1M Acceptance Rate 52.3% 




            
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lowenr than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n 

        while True:
            mid = (l + r ) // 2
            res = guess(mid)
            if res == -1:
                r = mid -1
            elif res == 1:
                l = mid + 1
            else:
                return mid 
            
# Runtime 41 ms Beats 78.9%
# Memory 16.3 MB Beats 36.26%  