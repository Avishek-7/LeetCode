class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}

        for letter in ransomNote:
            counts[letter] = counts.get(letter, 0) + 1

        for letter, count in counts.items():
            if count > magazine.count(letter):
                return False
        return True
        