class Solution:
    # Time o(n) and space o(n)
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for ast in asteroids:
            # Flag to indicate if a collision happened for the current asteroid
            collisionOccured = False  

            # Check for collision only if there's a positive asteroid in the stack
            # (stack[-1] > 0) and the current asteroid is negative (ast < 0),
            # which means they are moving towards each other
            while len(stack) != 0 and ast < 0 and stack[-1] > 0:
                # Compare the absolute sizes of the two asteroids
                if abs(ast) > stack[-1]:
                    # Current asteroid is larger, so it "destroys" the last asteroid in the stack
                    stack.pop()
                elif abs(ast) == stack[-1]:
                    # Both asteroids are equal in size, they both "explode"
                    collisionOccured = True # Mark that collision fully resolved this asteroid
                    stack.pop()  # Remove the last asteroid in the stack as both are destroyed
                    break  # Exit the loop as current asteroid is also destroyed
                else:
                    # The asteroid in the stack is larger, so the current asteroid is destroyed
                    collisionOccured = True  # Mark that collision fully resolved this asteroid
                    break  # Exit the loop as current asteroid is destroyed

            # If no collision occurred (i.e., the asteroid survived), add it to the stack
            if collisionOccured == False:
                stack.append(ast)

        return stack
