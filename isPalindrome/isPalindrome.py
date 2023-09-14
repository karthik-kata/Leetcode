class Solution:

    def isPalindrome(self, s: str) -> bool:
        r=""
        for c in s:
            if c.isalnum():
                r+=c
        r=r.lower()
        rev = r[::-1]
        if r == rev:
            return True
        else:
            return False
        