class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        write = 2

        for value in nums[2:]:
            if value != nums[write - 2]:
                nums[write] = value
                write += 1
        return write