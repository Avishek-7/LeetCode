class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        window_sum = 0
        max_sum = 0
        left = 0
        right = 0
        
        for right in range(len(arr)):
            window_sum += arr[right]
            
            if right >= k-1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[left]
                left += 1
        return max_sum