class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Find the target indices
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        return result