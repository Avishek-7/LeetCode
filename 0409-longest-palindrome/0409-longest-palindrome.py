class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        length = 0
        odd_found = False

        for count in counts.values():
            if count % 2 == 0:
                count -= count % 2
                length += count
            else:
                odd_found = True
                length += count - 1
        
        if odd_found:
            length += 1

        return length