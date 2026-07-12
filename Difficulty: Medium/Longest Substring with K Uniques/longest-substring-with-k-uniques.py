class Solution:
    def longestKSubstr(self, s, k):
        # code here
        char_count = {}
        left = 0
        max_length = -1
        
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            while len(char_count) > k:
                char_count[s[left]] -= 1
                
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            if len(char_count) == k:
                max_length = max(max_length, right - left + 1)
        return max_length
                 
        