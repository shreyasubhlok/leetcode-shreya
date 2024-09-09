class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        inDegree=[0]*numCourses
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course]=inDegree[course]+1
    
            
        topOrder=[]
        
        queue=deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                queue.append(i)
        
        while queue:
            currCourse=queue.popleft()
            topOrder.append(currCourse)
            
            for prereq in graph[currCourse]:
                inDegree[prereq]=inDegree[prereq]-1
                if inDegree[prereq]==0:
                    queue.append(prereq)
        
        return len(topOrder)==numCourses
        
        