class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        write_pos = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[write_pos] = left_square
                left += 1
                write_pos -= 1
            else:
                result[write_pos] = right_square
                right -= 1
                write_pos -= 1
        return result
        