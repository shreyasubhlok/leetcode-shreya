class Solution:
    '''
    BFS-Queue approach
    Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the number of edges. This is because in the worst case, every node
     and every edge is processed exactly once.
    Space Complexity: O(V + E) because:
        The adjacency list requires O(V + E) space to store the nodes and their neighbors.
        The visited list requires O(V) space.
        The queue can hold up to O(V) nodes in the worst case.
    '''
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialize adjacency list
        adjacencyList = [[] for i in range(n)]

        # Build the graph
        for e in edges:
            adjacencyList[e[0]].append(e[1])
            adjacencyList[e[1]].append(e[0])

        # BFS to find if a path exists from source to destination
        q = deque([source])
        visited = [False] * n
        visited[source] = True

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neighbor in adjacencyList[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        return False