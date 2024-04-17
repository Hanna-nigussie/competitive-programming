class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        non_zero_idx = 0
        for num in nums:
            if num != 0:
                nums[non_zero_idx] = num
                non_zero_idx += 1
        while non_zero_idx < n:
            nums[non_zero_idx] = 0
            non_zero_idx += 1
        
        return nums
