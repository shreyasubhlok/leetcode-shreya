class Solution:
    #problem-> Remember: The majority element occurs more than n // 2 times
    # preferred Approach- Moore's Voting Algorithm is the most efficient in terms of both time and space complexity.
    def majorityElement(self, nums: List[int]) -> int:
        # using Moore's voting algorithm
        """
        Time: o(n) and space :o(1)
        Algorithm:
        1.Initialize two variables: count and candidate. Set count to 0 and candidate to an arbitrary value.
        2.Iterate through the array nums:
           a. If count is 0, assign the current element as the new candidate and increment count by 1.
           b. If the current element is the same as the candidate, increment count by 1.
           c. If the current element is different from the candidate, decrement count by 1.
        3.After the iteration, the candidate variable will hold the majority element.
        """
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count = count + 1
            else:
                count = count - 1

        return candidate

    def majorityElementUsingSorting(self, nums: List[int]) -> int:
        """
        Time: O(NLogN) space:o(1) if inplace sorting otherwise o(n)
        """
        nums.sort()
        n = (len(nums) // 2)  # The majority element must be at the middle index after sorting. 
        return nums[n]

    def majorityElementUsingHashMap(self, nums: List[int]) -> int:
        """
        Time:O(N) and space:O(N) coz of myMap
        """
        myMap = {}
        # Populate the dictionary with frequencies
        for num in nums:
            if num in myMap:
                myMap[num] = myMap[num] + 1
            else:
                myMap[num] = 1

        """
        # Alternative, more concise way to update the dictionary:
        for num in nums:
            myMap[num]=myMap.get(num,0)+1
        """

        n = len(nums) // 2  # The majority element occurs more than n // 2 times
        # Use myMap.items() to get both keys and values and unpack them in the loop.
        # Use myMap.values() if you only need the values and not the keys.
        for num, value in myMap.items():
            if value > n:
                return num  # Return the element (key) that has a frequency greater than n // 2

        return -1  # This line is just a fallback; problem constraints guarantee a majority element
