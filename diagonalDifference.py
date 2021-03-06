import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    
    first_diagonal = 0
    second_diagonal = 0
    
    for i in range(0,n):
        first_diagonal += arr[i][i]
        second_diagonal += arr[i][n - i - 1]

    total = first_diagonal - second_diagonal
    return abs(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()