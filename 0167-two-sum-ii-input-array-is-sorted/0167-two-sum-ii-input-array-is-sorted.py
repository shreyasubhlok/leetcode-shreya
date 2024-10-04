class Solution:
    # two pointer technique
    # Time: o(n) and space=O(1) . In two sum porblem space is o(n) coz of hashmap
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low <= high:
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            if numbers[low] + numbers[high] < target:
                low = low + 1
            else:
                high = high - 1
        return [-1, -1]