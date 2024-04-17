class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        return lcm(2, n)