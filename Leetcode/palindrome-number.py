class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif int(str(x)[::-1]) == x:
            return True