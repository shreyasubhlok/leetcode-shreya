"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # BFS function to clone the graph
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Check if the input graph is empty
        if node is None:
            return node # Return None if there's no graph to clone

        # Dictionary to store cloned nodes. The key is the original node,  and the value is the corresponding cloned node.
        clonedNodesMap = {}

        # Initialize a queue for BFS traversal
        queue = deque()
        queue.append(node)  # Start BFS with the given node

        # Clone the start node and put it in the clonedNodeMap dictionary
        #The key would be the original node (let's say node with value 1). The value would be the newly cloned node, which is Node(1).
        clonedNodesMap[node] = Node(node.val)

        # BFS traversal
        while queue:
            currentNode = queue.popleft() # Pop the front node from the queue

            # Iterate over all neighbors of the current node
            for neighbor in currentNode.neighbors:
                if neighbor not in clonedNodesMap: # If the neighbor hasn't been cloned yet
                    # Clone the neighbor and add it to the dictionary
                    clonedNodesMap[neighbor] = Node(neighbor.val)
                    # Add the neighbor to the queue for BFS
                    queue.append(neighbor)

                # Add the cloned neighbor to the current cloned node's neighbors list
                clonedNodesMap[currentNode].neighbors.append(clonedNodesMap[neighbor])

        return clonedNodesMap[node]  # Return the cloned node corresponding to the input node