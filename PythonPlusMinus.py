#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    print(arr)
    cuentapositivo = 0
    cuentanegativo = 0
    cuentacero     = 0
    razonpositivo  = 0.000000
    razonnegativo  = 0.000000
    razoncero      = 0.000000
    n = len(arr)
    print(n)
    for x in arr:
        if x > 0:
            cuentapositivo = cuentapositivo + 1
        elif x < 0:
            cuentanegativo = cuentanegativo + 1    
        elif x == 0:
            cuentacero = cuentacero  + 1
    
    razonpositivo = cuentapositivo / n
    razonnegativo = cuentanegativo / n
    razoncero     = cuentacero / n
    
    print("{:.6f}".format(razonpositivo))
    print("{:.6f}".format(razonnegativo))   
    print("{:.6f}".format(razoncero))   
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)