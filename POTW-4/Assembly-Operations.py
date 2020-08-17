# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-04/challenges

#-----------------------------------------
#!/bin/python3

# Write code here
def assemblyOperation(length, iList):
    
    operations = [0]
    
    largest = 0
    
    for instructions in iList:
        if instructions[0] == "ADD":
            largest += int( instructions[1] )
            operations += [x+int( instructions[1] ) for x in operations]
            operations = [ min(operations), max(operations) ]
            operations += [largest]
            
        elif instructions[0] == "SQR":
            largest = largest ** 2
            operations += [x**2 for x in operations]
            operations = [ min(operations), max(operations) ]
            operations += [largest]
            
        elif instructions[0] == "LDI":
            largest = int( instructions[1] )
            operations += [largest]
            
    #print (operations) 
        
    print( max(operations))

#-------------------- Main ---------------------------
if __name__ == "__main__":
    
    num = int( input().strip() )
    
    instructions = []
    
    for x in range(num):
        instructions += [ input().strip().split() ]
        
    assemblyOperation(num, instructions)
    
