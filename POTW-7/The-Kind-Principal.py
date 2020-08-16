# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-07/challenges

#-----------------------------------------
#!/bin/python3

import os
import sys
import math

#------ Helper functions -----------------
def arithmeticProgression(term, start, diff):
    
    # Sum of Arithmetic Progression: Sn = (1/2)n [2a + (n-1)d]
    if (term == 1):
        return start
    total = (term / 2) * ( (2*start) + (( term - 1 ) * diff) )
    
    return int(total)

#------------------------------------------------------------------

# Complete the countTreats function below.
def countTreats(n, a, b, k):
    
    # The number of times the series will progress...
    # ...arithmetically from a or b (starting value)
    progress_up = (b - a) // k
    progress_down = (b - a) // k
    print ("progress up and down",progress_up,  progress_down)
    
    # Length of first half of the table
    length_up = progress_up + 1
    length_down = progress_down + 1

    # Sum of the increasing and decreasing sides
    sum_up = arithmeticProgression(length_up, a, k)
    sum_down = arithmeticProgression(length_down, b, -k)
    print ("sum up and down",sum_up, sum_down)
    
    # Overall sum of the increasing and decreasing sides
    o_sum = sum_up + sum_down
    
#-----------------------------------------------------------------
    # Length of the sequence 
    length = length_up + length_down
    
    # Number of times the sequence repeats in n
    multiplier =  n // length
    remainder = n % length 
    print ("multiplier and remainder", multiplier, remainder)
    
    # Total
    total = o_sum * multiplier
    
    #if (remainder == 0):
        #extra = 0
    if (remainder <= length_up):
        extra = arithmeticProgression(remainder, a, k)
        print("top half", extra)
    if (remainder > length_up):
        remainder -= length_up 
        extra = sum_up + arithmeticProgression(remainder, b, -k)
        print("bottom half", extra)
        
    #print("final table",treats_table)
    return total + extra

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nabk = input().split()

        n = int(nabk[0])

        a = int(nabk[1])

        b = int(nabk[2])

        k = int(nabk[3])

        result = countTreats(n, a, b, k)

        fptr.write(str(result) + '\n')

    fptr.close()
