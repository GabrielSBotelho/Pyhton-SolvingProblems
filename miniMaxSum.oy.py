import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    result = []
    for i in range(len(arr)):
        add = sum(arr) - arr[i]
        result.append(add)
    
    print(min(result), max(result))
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
