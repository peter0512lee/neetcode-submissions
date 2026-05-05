class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        if not s: return True
        head_p, tail_p = 0, len(s)-1
        
        while head_p <= tail_p:
            if s[head_p] != s[tail_p]:
                return False
            head_p += 1
            tail_p -= 1
        
        return True