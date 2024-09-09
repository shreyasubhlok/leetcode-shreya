from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        # Initialize in-degrees
        inDegree = [0] * numCourses
        
        # Build the graph and calculate in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course, directed edge
            inDegree[course] += 1  # Increment in-degree for the course
        
        # Initialize a queue with all nodes having zero in-degrees
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        # Process the nodes in the queue
        topOrder = []
        while queue:
            currCourse = queue.popleft()
            topOrder.append(currCourse)
            
            # Decrease the in-degree of neighboring nodes
            for neighbor in graph[currCourse]:
                inDegree[neighbor] -= 1
                # If in-degree becomes zero, add it to the queue
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if topological sort includes all nodes
        return len(topOrder) == numCourses
