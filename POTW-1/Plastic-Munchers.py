# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-01/challenges

#-----------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countMunchers' function below.
#
# The function is expected to return a 1D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER an
#  2. INTEGER ad
#  3. INTEGER b
#  4. INTEGER p0
#  5. INTEGER m0
#  6. INTEGER_ARRAY queries
#

def countMunchers(an, ad, b, p0, m0, queries):
    # Write your code here
    a = an/ad
    
    result = []
    
    for num in range( max(queries) ):
        
        ap = (a * p0)
        bap = (b * ap)
        m0 = m0 + bap
            
        p0 = p0 - ap
        
        result.append( int(m0) )
                
    return result

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    an = int(first_multiple_input[0])

    ad = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    p0 = int(second_multiple_input[0])

    m0 = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    b = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    queries = list(map(int, input().rstrip().split()))

    results = countMunchers(an, ad, b, p0, m0, queries)
    
    for number in queries:
        fptr.write(str( results[number-1] ) + "\n")
    
    fptr.close()
