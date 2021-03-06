import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    p1=0
    p2=0
    
    for i in range(0,3):
        if a[i] > b[i]:
            p1 += 1
        elif a[i] < b[i]:
            p2 += 1
        else:
            p1 = p1
            p2 = p2
    
    result = []
    result.append(p1)
    result.append(p2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
