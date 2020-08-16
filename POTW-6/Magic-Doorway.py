# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-06/challenges

#-----------------------------------------
#!/bin/python3

#Helper functions
def FIFO():
    return []

def isEmpty(queue):
    
    if (len(queue) == 0):
        return True
    
    return False

def enqueue(queue, element):
    queue.append(element)
    
def dequeue(queue):
    return queue.pop(0)
    
def nbrs(graph, key):
    return graph[key]

#----------------------------------------------------------

#Professor Coore's BFS
# def bfsVisit(graph, start=0, status={}, src={}):
#     q = FIFO()
#     q.enqueue(start)
#     status[start] = "Discovered"
#     while( not q.isEmpty() ):
#         u = q.dequeue()
#         status[u] = "Visited"
#         for v in graph.nbrs(u):  
#             if status[v] == "Unseen":
#                 q.enqueue(v)       
#                 status[v] = "Discovered"    
#                 src[v] = u

    
def MagicDoorWay(graph, locations, l_num):
    
    # Creates Sets
    # A set is a collection which is unordered and unindexed.
    # In Python sets are written with curly brackets.
    next_nodes = set()
    temp = set()
    
    count = 0
    
    # Adds a nodes neighbors to the set, doesn't add duplicates
    next_nodes.update( graph[count] )
    
    while( count < l_num ):
        #print(count)
    
        if (locations[count] in next_nodes):
            #print(locations[count], "", count)
            result = [ locations[count], count ]
            print(" ".join(str(x) for x in result))
            break
        
        count += 1
        temp = next_nodes.copy()
        # Empties the Set
        next_nodes.clear()
            
        for x in temp:
            # Updates set with all possible neighbors
            next_nodes.update( graph[x] )
        #print(next_nodes)
            
    # print("It broke")
    

# Main
if __name__ == "__main__":
    
    # Adds a neighboring node to the list of neighbors
    def addNBRS(dictionary, key, value):
        dictionary[key].append(value)
    
    nms = list(map(int, input().rstrip().split()))
    n = nms[0]
    m = nms[1]
    s = nms[2]
    
    # List of locations
    location_list = list(map(int, input().rstrip().split()))
    
    # Key is the hour, Value is the location
    time_location = {}
    
    for hour in range(n):
        time_location[hour] = location_list[hour]
        
    connections = {0: [s]}
    
    for key in range(1, m):
        connections[key] = []
    
    for connection in range(m):
        nodes = list(map(int, input().rstrip().split()))
        addNBRS(connections, nodes[0], nodes[1])
        addNBRS(connections, nodes[1], nodes[0])
    # print(connections)
    # print(time_location)
    
    MagicDoorWay(connections, time_location, n)
    
