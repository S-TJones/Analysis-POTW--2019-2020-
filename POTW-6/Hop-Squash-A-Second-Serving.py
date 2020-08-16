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

def bfsVisit(graph, start, status):
    
    q = FIFO()
    count = 0
  
    enqueue(q, start) 
    status[start] = "Discovered"

    while( not isEmpty(q) ):
        
        start = dequeue(q)
        
        #if start in squash:
        count += nbrs(patches, start)
        
        for n in nbrs(graph, start): 
            
            if status[n] == "Unseen": 
                enqueue(q, n)
                status[n] = "Discovered"

    print(count)

# Main
if __name__ == "__main__":
    
    # Adds a neighboring node to the list of neighbors
    def addNBRS(dictionary, key, value):
        dictionary[key].append(value)
    
    num_vegetables = int( input() )
    # squash = []

    for num in range(num_vegetables):
        if ( input() == "Butternut Squash" ):
            # Stores the key that has "Butternut Squash"
            butter = num
        
    patches = {0: 0}
    node_status = {0: "Unseen"}
    connections = {0: []}
    
    patch_num = int( input() )
    for num in range(1, patch_num+1):
        # Each pair has the vegetable and amount
        veg_amt = list(map(int, input().rstrip().split()))
        
        if veg_amt[0] == butter:
            patches[num] = veg_amt[1]
        else:
            patches[num] = 0
        
        node_status[num] = "Unseen"
        connections[num] = []
    # print(patches)
    # print(squash)
        
    connection_num = int( input() )
    
    for num in range(connection_num):
        nodes = list(map(int, input().rstrip().split()))
        addNBRS(connections, nodes[0], nodes[1])
        addNBRS(connections, nodes[1], nodes[0])
    #print(connections)
    
    bfsVisit(connections, 0, node_status)
    
