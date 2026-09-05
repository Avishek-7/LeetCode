class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        result = []
        for char in s:
            if char != c:
                result.append(char)
        return "".join(result)