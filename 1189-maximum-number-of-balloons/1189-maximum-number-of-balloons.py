class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        text_count = {}

        for char in text:
            if char in balloon_count:
                text_count[char] = text_count.get(char, 0) + 1
        
        return min(text_count.get('b', 0), text_count.get('a', 0), text_count.get('l', 0) // 2, text_count.get('o', 0) // 2, text_count.get('n', 0))