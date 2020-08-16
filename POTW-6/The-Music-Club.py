# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-06/challenges

#-----------------------------------------
#
import itertools

#
def MusicClub(pref, ranked, n, k, r):
    
    p_list = []
    small_i = 1000000000
    small_v = 1000000000

    # Stores Member 1 list of songs
    m1 = ranked[1]
    p1 = pref[1]

#--------- This section Generates a list of Preference Differences --------------
    
    # Loops through every other member except the first
    for member in range(2, n+1):
        
        # Copies the other members
        temp = pref[member].copy()
        
        count = 0
        
        # For every number in the members' 1 Preference list
        for num in p1:
            
            # Gives a list of elements from the beginning to the current num
            temp1 = temp[:temp.index(num)]
            
            # Remove the current num from the list
            temp.remove(num)
            
            # Counts the number of preference differences
            count += len(temp1)
        
        # Adds the preference difference number to the list
        p_list.append(count)

#--------- This section determines the Smallest Recommended Song --------------

    # Gets the smallest preference difference
    small = min(p_list)
    
    # Gets all index numbers of the smallest preference difference
    indices = [i+2 for i, x in enumerate(p_list) if x == small]

    # List to store the recommended song
    recommendations = -1
    
    for key in indices:
        # Gets list of all recommended songs not in the first members list
        temp = set(ranked[key]) - set(m1)
        first = [item for item in ranked[key] if item in temp]
        #print(temp, first)
        
        #for num in first:
        # Gets the index number of each recommended song
        x = ranked[key].index(first[0])
        
        corresponding = pref[key][x]
        
        # If the song has the lowest index number
        if corresponding <= small_i:

            # if -1 in recommendations:
            #     # Remove -1 and add the new recommended song
            #     recommendations.remove(-1)

            # It becomes the new lowest
            small_i = corresponding

            recommendations = ranked[key][x]

    # Return the small recommendation
    return recommendations

#-----------------------------------------------------------------------------

# Main
if __name__ == "__main__":
    
    kr = list(map(int, input().rstrip().split()))
    k = kr[0]
    r = kr[1]
    
    n = int( input() )
    
    members_p = {}
    members_r = {}
    
    for num in range(1, n+1):
        members_p[num] = list(map(int, input().rstrip().split()))
        members_r[num] = list(map(int, input().rstrip().split()))
    
    result = MusicClub(members_p, members_r, n, k, r)
    print(result)
    
