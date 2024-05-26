class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_freq = {}
        operations = 0
        
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 0
            num_freq[num] += 1
        
        unique_nums = set(nums)
        
        for num in unique_nums:
            complement = k - num
            if complement in num_freq and num_freq[complement] > 0:
                if complement != num:  # Ensure we don't double-count if complement == num
                    min_freq = min(num_freq[num], num_freq[complement])
                    operations += min_freq
                    num_freq[num] -= min_freq
                    num_freq[complement] -= min_freq
                else:
                    operations += num_freq[num] // 2
                    num_freq[num] -= num_freq[num] // 2
        
        return operations