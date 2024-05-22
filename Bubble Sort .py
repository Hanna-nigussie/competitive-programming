#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    num_swaps = 0
    n = len(a)
    
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                # Swap adjacent elements if they are in decreasing order
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
    
    # After sorting, print the required information
    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
