import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('\W','',s)
    
    return s == s[::-1]