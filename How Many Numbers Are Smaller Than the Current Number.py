
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for num in nums:
            count[num] += 1
        
        prefix_sum = [0] * 101
        for i in range(1, 101):
            prefix_sum[i] = prefix_sum[i-1] + count[i-1]
        
        result = []
        for num in nums:
            result.append(prefix_sum[num])
        
        return result