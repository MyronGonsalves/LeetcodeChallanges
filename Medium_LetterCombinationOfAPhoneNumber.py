# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# Accepted 1.6M Submissions 2.8M Acceptance Rate 57.3%   


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz" } 

        def backtrack(i,curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return 
            for c in digitToChar[digits[i]]:
                backtrack(i+1,curStr +c)

        if digits:
            backtrack(0,"")

        return res   
    
# Runtime 44 ms Beats 74%
# Memory 16.4 MB Beats 19.21% 