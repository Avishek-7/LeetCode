class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        fruit_count = {}
        left = 0
        max_length = 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

            while len(fruit_count) > k:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
        