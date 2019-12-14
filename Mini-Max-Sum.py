import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    max_input = sum(arr) - min(arr)
    min_input = sum(arr) - max(arr)
    
    print(f"{min_input} {max_input}")
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
