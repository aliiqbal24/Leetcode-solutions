# Notes
# First we me must initialize the clean the string, this will be: removing spaces,
# punctuaition and treating capitals as no different
# once cleaned we can reverse the string and compare it to the cleaned
# if they are the same string then it is a valid palindrome, if not: invalid

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        
        for char in s:
            if char.isalnum():  
             clean += char.lower()
        
        return clean == clean[::-1]
