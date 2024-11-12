class Solution:
    # The time complexity is O(T log k), where T is the total number of tasks and k is the number of unique tasks.
    # Space complexity is O(k + n), where k is the unique tasks and n is the cooldown period.
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        # Step 2: Initialize a max heap based on task frequencies (invert values for max heap behavior)
        maxHeap = []
        for value in freq.values():
            heapq.heappush(maxHeap, -value)

        queue = deque()  # Queue to manage cooldown tasks (task count, eligible time)
        timer = 0  # Global timer to track total time

        # Step 3: Process tasks and manage cooldowns
        while maxHeap or queue:
            # Schedule the most frequent task if available
            if maxHeap:
                # Retrieve and remove the task with the highest frequency
                task = -heapq.heappop(maxHeap)

                # If more occurrences are left, add to cooldown with the next eligible time
                if task > 1:
                    queue.append((task - 1, timer + n + 1))

            # Increment the timer after scheduling or idle time
            timer += 1

            # Step 4: Check cooldown queue to reschedule tasks that are ready
            if queue and queue[0][1] == timer:
                # Retrieve the task that is ready to be rescheduled
                cooldownTask = queue.popleft()
                taskReadyToReschedule = cooldownTask[0]

                # Re-add the task to the heap to be scheduled again
                heapq.heappush(maxHeap, -taskReadyToReschedule)

        # Return the total time taken to schedule all tasks
        return timer