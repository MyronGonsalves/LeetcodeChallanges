# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.
# Accepted 159.2K Submissions 263.1K Acceptance Rate 60.5%  


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = text.count('l')//2
        o = text.count('o')//2
        n = text.count('n')

        return min(b,a,l,o,n) 
    

# Runtime 40 ms Beats 91.51%
# Memory 16.3 MB Beats 93.90%  