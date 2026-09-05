class Solution:
    def isPalindrome(self, s):
        # code here
        def helper(left: int, right: int) -> bool:
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return helper(left+1, right-1)
        return helper(0, len(s)-1)
