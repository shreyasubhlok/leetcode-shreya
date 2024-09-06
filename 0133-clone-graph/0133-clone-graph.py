"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        clonedDict={}
        queue=deque()
        queue.append(node)
        
        clonedDict[node]=Node(node.val)
        
        while queue :
            currNode=queue.popleft()
            
            for neighbor in currNode.neighbors:
                if neighbor not in clonedDict:
                    clonedDict[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                
                clonedDict[currNode].neighbors.append(clonedDict[neighbor])
        
        return clonedDict[node]
        
        
        