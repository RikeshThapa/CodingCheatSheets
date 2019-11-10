#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    z = 0
    #the resultant array, indicating pairs of each colour 
    for x in ar:
        if z != 1:
            key = [x]
            count = [1]
            z =1
        else:
            if x in key:
                count[key.index(x)] = count[key.index(x)]+1 
            else:
                key.append(x)
                count.append(1)
    count = map(calcualtor, count)
    return int(sum(count))
def calcualtor(i):
    y = (i-(i%2))/2
    return y




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
