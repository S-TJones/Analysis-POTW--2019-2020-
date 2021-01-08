# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-02/challenges

#-----------------------------------------
#!/bin/python3

# Write code here
import bisect

def determineIndex(volumes, volume_lst, queries_lst):    
    
    total = 0
    prefix_sum_list = []
    
    for volume in volume_lst:
        total += volume
        prefix_sum_list += [ total ]
        
    for query_num in queries_lst:
        # Naiive Way -------------------------------
        # if sum(volume_lst) < query_num:
        #     print(-1)
        # elif sum(volume_lst) == query_num:
        #     print(volumes)
        # else:
        #     print( bisect.bisect_left(prefix_sum_list, query_num) + 1 )
        #-------------------------------------------
        
        length = len(prefix_sum_list) - 1
        position = 0
        found = False
        
        # Binary Search
        while(position <= length):
            
            # Check if query_num matches the first element
            if(prefix_sum_list[position] >= query_num):
                print(position + 1)
                found = True
                break
                
            middle = int( position + (length - position)/2 )
            
            # Check if query_num is present at the middle
            if(prefix_sum_list[middle] == query_num):
                print(middle + 1)
                found = True
                break
                
            # If it's not middle, go left or right
            if(prefix_sum_list[middle] > query_num):
                # Focus on the right side
                length = middle
                position += 1
            else:
                # Focus on the right side
                position = middle + 1
                
        # If query_num isn't found
        if(found != True):
            print("-1")

# Main
if __name__ == "__main__":
    
    volumes = int( input() )
    
    volume_lst = list(map(int, input().rstrip().split()))
    
    queries = int( input() )
    
    queries_lst = list(map(int, input().rstrip().split()))
    
    # Call function
    determineIndex(volumes, volume_lst, queries_lst)