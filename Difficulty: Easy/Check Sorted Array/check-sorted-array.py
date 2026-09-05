class Solution:
    def isSorted(self, arr):
        # code here
        def helper(index: int) -> bool:
            if index >= len(arr)-1:
                return True
            if arr[index]>arr[index+1]:
                return False
            return helper(index+1)
        return helper(0)