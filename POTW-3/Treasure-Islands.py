# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2020-potw-03/challenges

#-----------------------------------------------
#!/bin/python3

#------------------ Helper functions ----------------
import sys

def cons(x, y):
    return [x, y]

def car(p):
    return p[0]

def cdr(p):
    return p[1]

nil = []

def makeBinTree(root, left, right):
    return cons(left, cons(root, right))

emptyTree = nil

# Enter your code here. Return your answer do not print it

def isEmpty(tree):
    # Complete this function
    if tree == emptyTree:
        return True
    return False

def root(tree):
    # Complete this function
    return car(cdr(tree))

def left(tree):
    # Complete this function
    return car(tree)

def right(tree):
    # Complete this function
    return cdr(cdr(tree))
    
#---------------------------------------------------

def findMaxTreasure(tree, secret, ptotal):
    # Complete this function
    def isLeaf(tree):
        if isEmpty(left(tree)) and isEmpty(right(tree)):
            return True
        return False

    def Treasure_Count(ptotal, Treasures):
        if ptotal%secret == 0:
            Treasures += 1
            return Treasures
        return Treasures

    def Find_Treasure(tree, Treasures, ptotal):
        if isEmpty(tree):
            return 0
        else:
            ptotal = root(tree) + ptotal
            Treasures = Treasure_Count(ptotal, Treasures)
            if isLeaf(tree):
                return Treasures
            else:
                return max(Find_Treasure(left(tree), Treasures, ptotal), Find_Treasure(right(tree), Treasures, ptotal))

    Treasures = 0
    T = Find_Treasure(tree, Treasures, ptotal)
    return T

#-------------------- Main ---------------------

if __name__=="__main__":
    n, s = input().strip().split(' ')
    n, s = int(n), int(s)
    nodes = [None] * (n+1)
    nodes[0] = emptyTree
    for i in range(n):
        i, v, j, k = list(map(int, input().strip().split(' ')))
        nodes[i] = makeBinTree(v, nodes[j], nodes[k])
    r = findMaxTreasure(nodes[1], s, 0)
    print(r)
