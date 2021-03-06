import math
import os
import random
import re
import sys

def findDigits(n):
    count = 0
    aux = 0
    num_to_list = str(n)
    
    for i in num_to_list:
        aux = int(i)
        if aux != 0 and n != 0:
            if n % aux == 0:
                count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
