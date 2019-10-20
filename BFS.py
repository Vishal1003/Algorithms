import numpy as np
tree = {'A':['B', 'C'], 'B':['D', 'E'], 'C':['F', 'G'], 'D':['H', 'I'], 'E':['J', 'K'], 'F':['L', 'M'], 'G':['N', 'O']}

def bfs(tree, node):
    l = []
    while node != None:
        print(node)
        try:
            if node not in tree.keys():
                node = l.pop(0)
            else:
                l.append(tree[node][0])
                l.append(tree[node][1])
                node = l.pop(0)
        except IndexError:
            break
    
#This is a python implementation of the Breadth First Search (BFS) Algortihm.
