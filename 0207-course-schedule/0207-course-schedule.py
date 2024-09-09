class Solution:
    '''
    Check image file dry run in lithub
    Time: o(v+e) overall
        Step 1: Calculate In-degree of Each Node -> o(v+e)
        step 2:Step 2: Initialize the Queue and Add All 0 In-degree Vertices -> o(v)
        Step 3: Process Vertices in BFS Manner -> o(v)
    space: o(v+e) overall
        In-degree Array (inDegree) -> o(v)
        Queue->o(v)
        Adjacency List (self.graph) -> o(v+e)
        Topological Order List (topoOrder) -> o(v)
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # STEP 1: create an adjacency list to represent directed graph
        # Required initializations for this code
        adjList = [[] for i in range(numCourses)]
        inDegrees = [0] * len(adjList)  # Initialize in-degrees array
        topoOrder = []  # res list to store the topological order (if valid)
        queue = deque()
        
        
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            # It's required to store links
            adjList[prereq].append(course)  # prereq -> course, directed edge
            inDegrees[course] += 1  # Increment the in-degree for each course
            # STEP 2: create an array in degrees to store the no of edges for each node in graph

        # STEP 3: Add all nodes with zero indegree to queue
        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:  # Add courses which have no prerequisites and can be started immediately
                queue.append(i)

        # STEP 4: Process nodes in BFS manner
        while queue:
            currCourse = queue.popleft()  # Get a course with no remaining prerequisites
            topoOrder.append(currCourse)  # Add to topological sort order
            # For each neighboring course (dependent course)
            for prereq in adjList[currCourse]:
                inDegrees[prereq] -= 1  # Decrease the in-degree

                # It means that prerequisite of this course is done and
                # it can be started immediately
                if inDegrees[prereq] == 0:  # If in-degree is now 0, add to queue
                    queue.append(prereq)

        # If topoOrder contains all courses, it means there's no cycle, and all courses can be finished
        return len(topoOrder) == numCourses