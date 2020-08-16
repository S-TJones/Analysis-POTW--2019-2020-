# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-06/challenges

#-----------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

# import Counter from collections 
from collections import Counter

# Complete the 'investigate' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER m
#  4. INTEGER x0
#  5. INTEGER n
#  6. 2D_INTEGER_ARRAY queries
#

def investigate(a, b, m, x0, n, queries):
    # Write your code here
    
    first_set = [x0]
    #hashed_values = []
    #frequencies = []
    
    for num in range(n-1):
        xi = ( (a*x0) + b) % m
        first_set.append(xi)
        x0 = xi
    
    c = Counter(first_set)
        
    for query in queries:
        count = 0
        low = (query[1] * m) / query[0]
        #print(low)
        low = math.ceil(low)
        high = ((query[1] + 1) * m) / query[0]
        #print(high)
        high = math.ceil(high)
        
        range_list = list( range(low, high) )
        
        for num in range_list:
            count += c[num]
        print(count)
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()
    
    a = int(first_multiple_input[0])
    
    b = int(first_multiple_input[1])
    
    m = int(first_multiple_input[2])
    
    x0 = int(first_multiple_input[3])
    
    second_multiple_input = input().rstrip().split()
    
    n = int(second_multiple_input[0])
    
    q = int(second_multiple_input[1])
    
    queries = []
    
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
        
    #result = 
    investigate(a, b, m, x0, n, queries)
    
    #fptr.close()
