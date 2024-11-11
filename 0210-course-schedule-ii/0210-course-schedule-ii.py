class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        inDegrees = [0] * len(adjList)
        topoOrder = []
        queue = deque()

        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            adjList[prereq].append(course)
            inDegrees[course] += 1

        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                queue.append(i)

        while queue:
            currCourse = queue.popleft()
            topoOrder.append(currCourse)
            for prereq in adjList[currCourse]:
                inDegrees[prereq] -= 1

                if inDegrees[prereq] == 0:
                    queue.append(prereq)

        if len(topoOrder) == numCourses:
            return topoOrder
        else:
            return []