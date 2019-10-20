import numpy as np
tree = {'A':['B', 'C'], 'B':['D', 'E'], 'C':['F', 'G'], 'D':['H', 'I'], 'E':['J', 'K'], 'F':['L', 'M'], 'G':['N', 'O']}

def dfs(tree, root, pos):
    print(root)
    
    if root in tree:
        dfs(tree, tree[root][0], 0)
        dfs(tree, tree[root][1], 1)

#This is a Recursive Implementation of the Depth First Search (DFS) Algorithm to traverse a tree.
#The tree here is implemented in the for of a dictionary, but it could have also been used as a class
#Following is a class to make a tree node. 

#class TreeNode:
#   def __init__(self, data):
#       self.value = data
#       self.left = None
#       self.right = None

#and use this to create a Tree: 
