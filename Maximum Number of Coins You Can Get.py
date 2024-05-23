class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #  Sort the piles in descending order
        piles.sort(reverse=True)
        
        #  Initialize the result to zero
        max_coins = 0
        
        # Iterate through the sorted piles
        n = len(piles) // 3  # The number of steps we need to perform
        for i in range(n):
            # Picking the second largest pile in each triplet
            max_coins += piles[2 * i + 1]
        
        return max_coins