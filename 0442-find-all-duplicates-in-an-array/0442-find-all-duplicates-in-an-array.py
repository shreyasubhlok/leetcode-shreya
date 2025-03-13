class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        res = []
        for elem in nums:
            if elem in visited:
                res.append(elem)
            visited.add(elem)
        return res     